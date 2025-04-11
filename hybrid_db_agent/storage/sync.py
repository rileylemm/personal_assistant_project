import logging
import os
import sys
from typing import Dict, List, Any, Optional, Union, Tuple
import uuid
import time
from datetime import datetime

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config
from storage.neo4j_client import Neo4jClient, get_neo4j_client
from storage.qdrant_client import QdrantClientWrapper, get_qdrant_client
from core.embedding import EmbeddedChunk

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('db_sync')

class DatabaseSynchronizer:
    """
    Synchronizes data between Neo4j graph database and Qdrant vector database.
    """
    def __init__(
        self,
        neo4j_client: Optional[Neo4jClient] = None,
        qdrant_client: Optional[QdrantClientWrapper] = None
    ):
        """
        Initialize database synchronizer.
        
        Args:
            neo4j_client: Neo4j client instance (created if not provided)
            qdrant_client: Qdrant client instance (created if not provided)
        """
        self.neo4j = neo4j_client or get_neo4j_client()
        self.qdrant = qdrant_client or get_qdrant_client()
        logger.info("Initialized database synchronizer")
    
    def store_embedded_chunks(self, embedded_chunks: List[EmbeddedChunk], document_id: str) -> List[str]:
        """
        Store embedded chunks in both Neo4j and Qdrant.
        
        Args:
            embedded_chunks: List of embedded chunks
            document_id: ID of the parent document
            
        Returns:
            List of chunk IDs
        """
        if not embedded_chunks:
            logger.warning("No embedded chunks provided for storage")
            return []
        
        logger.info(f"Storing {len(embedded_chunks)} embedded chunks for document {document_id}")
        
        # Step 1: Store embeddings in Qdrant
        vectors = [chunk.embedding for chunk in embedded_chunks]
        
        # Prepare metadata with proper IDs
        metadata_list = []
        chunk_ids = []
        for chunk in embedded_chunks:
            # Generate chunk_id if not present
            if 'chunk_id' not in chunk.metadata:
                chunk.metadata['chunk_id'] = str(uuid.uuid4())
            
            # Store both the chunk ID and document ID in both databases
            metadata = chunk.metadata.copy()
            metadata['document_id'] = document_id
            metadata['text'] = chunk.text  # Store text in Qdrant for easier retrieval
            metadata['stored_at'] = datetime.now().isoformat()
            
            metadata_list.append(metadata)
            chunk_ids.append(metadata['chunk_id'])
        
        # Upsert into Qdrant
        try:
            qdrant_ids = self.qdrant.upsert_points(vectors, metadata_list)
            logger.info(f"Stored {len(qdrant_ids)} vector embeddings in Qdrant")
        except Exception as e:
            logger.error(f"Failed to store embeddings in Qdrant: {str(e)}")
            raise
        
        # Step 2: Store the document and chunks in Neo4j
        try:
            # Create/update the document node
            self.neo4j.create_document({'document_id': document_id})
            
            # Create chunk nodes and link to document
            for chunk, qdrant_id in zip(embedded_chunks, qdrant_ids):
                # Add the Qdrant ID to the metadata
                chunk_metadata = chunk.metadata.copy()
                chunk_metadata['qdrant_id'] = qdrant_id
                
                # Store in Neo4j
                self.neo4j.create_chunk(chunk.text, chunk_metadata, document_id)
            
            logger.info(f"Stored {len(embedded_chunks)} chunks in Neo4j")
            return chunk_ids
        
        except Exception as e:
            logger.error(f"Failed to store chunks in Neo4j: {str(e)}")
            # Try to rollback Qdrant changes
            try:
                self.qdrant.delete_points(qdrant_ids)
            except:
                pass
            raise
    
    def delete_document(self, document_id: str) -> bool:
        """
        Delete a document and all its chunks from both databases.
        
        Args:
            document_id: Document ID
            
        Returns:
            bool: True if successful
        """
        logger.info(f"Deleting document {document_id} from all databases")
        
        # Step 1: Get all chunks for the document from Neo4j
        try:
            chunks = self.neo4j.get_document_chunks(document_id)
            qdrant_ids = [chunk.get('qdrant_id') for chunk in chunks if chunk.get('qdrant_id')]
            logger.info(f"Found {len(qdrant_ids)} Qdrant IDs for document {document_id}")
        except Exception as e:
            logger.error(f"Error retrieving document chunks: {str(e)}")
            return False
        
        # Step 2: Delete from Qdrant
        if qdrant_ids:
            try:
                self.qdrant.delete_points(qdrant_ids)
                logger.info(f"Deleted {len(qdrant_ids)} points from Qdrant")
            except Exception as e:
                logger.error(f"Error deleting from Qdrant: {str(e)}")
                return False
        
        # Step 3: Delete from Neo4j
        try:
            self.neo4j.delete_document(document_id)
            logger.info(f"Deleted document {document_id} from Neo4j")
            return True
        except Exception as e:
            logger.error(f"Error deleting from Neo4j: {str(e)}")
            return False
    
    def search_similar(self, query_vector, filter_dict=None, limit=10):
        """
        Search for similar documents across both databases.
        
        Args:
            query_vector: Query embedding vector
            filter_dict: Optional filter criteria
            limit: Maximum number of results
            
        Returns:
            List of results with combined information
        """
        # Step 1: Search for similar vectors in Qdrant
        try:
            results = self.qdrant.search_similar(query_vector, filter_dict, limit)
            logger.info(f"Found {len(results)} similar vectors in Qdrant")
            
            if not results:
                return []
            
            # Step 2: Enhance with Neo4j information
            enhanced_results = []
            for result in results:
                try:
                    # Get chunk ID from Qdrant payload
                    chunk_id = result['payload'].get('chunk_id')
                    if not chunk_id:
                        enhanced_results.append(result)
                        continue
                    
                    # Query Neo4j for additional context
                    query = """
                    MATCH (c:Chunk {chunk_id: $chunk_id})<-[:CONTAINS]-(d:Document)
                    OPTIONAL MATCH (h:Header)-[:CONTAINS]->(c)
                    RETURN d.title AS document_title,
                           d.document_id AS document_id,
                           h.title AS header_title,
                           h.level AS header_level
                    """
                    
                    with self.neo4j.driver.session(database=self.neo4j.database) as session:
                        neo4j_result = session.run(query, chunk_id=chunk_id).single()
                        
                        if neo4j_result:
                            # Add Neo4j data to result
                            result['document_title'] = neo4j_result.get('document_title')
                            result['document_id'] = neo4j_result.get('document_id')
                            result['header_title'] = neo4j_result.get('header_title')
                            result['header_level'] = neo4j_result.get('header_level')
                        
                    enhanced_results.append(result)
                
                except Exception as e:
                    logger.error(f"Error enhancing result with Neo4j data: {str(e)}")
                    enhanced_results.append(result)
            
            return enhanced_results
            
        except Exception as e:
            logger.error(f"Error searching similar vectors: {str(e)}")
            raise
    
    def close(self):
        """
        Close both database connections.
        """
        try:
            self.neo4j.close()
            self.qdrant.close()
            logger.info("Closed all database connections")
        except Exception as e:
            logger.error(f"Error closing database connections: {str(e)}")

# Factory function to get database synchronizer
def get_db_sync() -> DatabaseSynchronizer:
    """
    Factory method to get a database synchronizer instance.
    
    Returns:
        DatabaseSynchronizer instance
    """
    return DatabaseSynchronizer()

# Example usage
if __name__ == "__main__":
    # This example demonstrates how to use the synchronizer
    # but requires the actual embedded chunks from the embedding module
    
    print("DatabaseSynchronizer Example")
    print("----------------------------")
    print("Note: This is a demonstration file and requires actual embedded chunks.")
    print("To see it in action, run the complete processing pipeline.")
    
    try:
        # Create a database synchronizer
        synchronizer = get_db_sync()
        
        # Example document
        document_id = "example-doc-123"
        
        # We would normally get these from the embedding module
        # embedded_chunks = [...]
        
        # Delete any existing document with this ID for demonstration
        synchronizer.delete_document(document_id)
        
        print(f"Created database synchronizer.")
        print(f"In a real workflow, it would store embedded chunks in both Neo4j and Qdrant.")
        print(f"See the workers module for the complete processing flow.")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Close connections
        synchronizer.close() 