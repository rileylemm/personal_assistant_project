import logging
import os
import sys
from typing import Dict, List, Any, Optional, Union
import uuid
import json

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config

# Import Neo4j driver
try:
    from neo4j import GraphDatabase, Driver, Session, Transaction, Result
    from neo4j.exceptions import Neo4jError
except ImportError:
    logging.error("Neo4j driver not installed. Run 'pip install neo4j'")
    raise

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('neo4j_client')

class Neo4jClient:
    """
    Client for interacting with Neo4j graph database.
    """
    def __init__(
        self,
        uri: str = Config.NEO4J.URI,
        user: str = Config.NEO4J.USER,
        password: str = Config.NEO4J.PASSWORD,
        database: str = Config.NEO4J.DATABASE
    ):
        """
        Initialize Neo4j connection.
        
        Args:
            uri: Neo4j connection URI (bolt://host:port)
            user: Neo4j username
            password: Neo4j password
            database: Neo4j database name
        """
        self.uri = uri
        self.user = user
        self.password = password
        self.database = database
        self._driver = None
        logger.info(f"Initializing Neo4j client for {uri}")
    
    @property
    def driver(self) -> Driver:
        """
        Lazy-load the Neo4j driver.
        """
        if self._driver is None:
            try:
                self._driver = GraphDatabase.driver(
                    self.uri,
                    auth=(self.user, self.password)
                )
                # Verify connection
                self._driver.verify_connectivity()
                logger.info("Successfully connected to Neo4j database")
            except Exception as e:
                logger.error(f"Failed to connect to Neo4j: {str(e)}")
                raise
        return self._driver
    
    def close(self) -> None:
        """
        Close the Neo4j driver connection.
        """
        if self._driver is not None:
            self._driver.close()
            self._driver = None
            logger.info("Neo4j connection closed")
    
    def create_document(self, document_metadata: Dict[str, Any]) -> str:
        """
        Create a new document node in Neo4j.
        
        Args:
            document_metadata: Dictionary containing document metadata
            
        Returns:
            str: Document ID
        """
        # Ensure document_id is present
        if 'document_id' not in document_metadata:
            document_metadata['document_id'] = str(uuid.uuid4())
        
        document_id = document_metadata['document_id']
        
        query = """
        MERGE (d:Document {document_id: $document_id})
        SET d += $metadata
        RETURN d.document_id AS document_id
        """
        
        with self.driver.session(database=self.database) as session:
            try:
                result = session.run(
                    query,
                    document_id=document_id,
                    metadata=document_metadata
                )
                record = result.single()
                if record:
                    logger.info(f"Created/updated document node with ID: {document_id}")
                    return record["document_id"]
                else:
                    raise Exception("Failed to create document node")
            except Exception as e:
                logger.error(f"Error creating document node: {str(e)}")
                raise
    
    def create_chunk(self, chunk_text: str, chunk_metadata: Dict[str, Any], document_id: str) -> str:
        """
        Create a new chunk node in Neo4j and link it to its document.
        
        Args:
            chunk_text: The text content of the chunk
            chunk_metadata: Dictionary containing chunk metadata
            document_id: ID of the parent document
            
        Returns:
            str: Chunk ID
        """
        # Ensure chunk_id is present
        if 'chunk_id' not in chunk_metadata:
            chunk_metadata['chunk_id'] = str(uuid.uuid4())
        
        chunk_id = chunk_metadata['chunk_id']
        
        # Create a query that creates the chunk and links it to the document
        query = """
        MATCH (d:Document {document_id: $document_id})
        MERGE (c:Chunk {chunk_id: $chunk_id})
        SET c.text = $text,
            c += $metadata
        MERGE (d)-[:CONTAINS]->(c)
        """
        
        # If header information is present, create/link to header node
        if 'header_title' in chunk_metadata and 'header_level' in chunk_metadata:
            query += """
            MERGE (h:Header {
                document_id: $document_id,
                title: $header_title,
                level: $header_level
            })
            MERGE (d)-[:HAS_HEADER]->(h)
            MERGE (h)-[:CONTAINS]->(c)
            """
        
        query += "RETURN c.chunk_id AS chunk_id"
        
        with self.driver.session(database=self.database) as session:
            try:
                result = session.run(
                    query,
                    document_id=document_id,
                    chunk_id=chunk_id,
                    text=chunk_text,
                    metadata=chunk_metadata,
                    header_title=chunk_metadata.get('header_title'),
                    header_level=chunk_metadata.get('header_level')
                )
                record = result.single()
                if record:
                    logger.info(f"Created chunk node with ID: {chunk_id}")
                    return record["chunk_id"]
                else:
                    raise Exception("Failed to create chunk node")
            except Exception as e:
                logger.error(f"Error creating chunk node: {str(e)}")
                raise
    
    def link_chunks_to_qdrant(self, chunk_ids: List[str], qdrant_ids: List[str]) -> None:
        """
        Link chunk nodes to their corresponding vector embeddings in Qdrant.
        
        Args:
            chunk_ids: List of Neo4j chunk IDs
            qdrant_ids: List of Qdrant point IDs
        """
        if len(chunk_ids) != len(qdrant_ids):
            raise ValueError("chunk_ids and qdrant_ids must have the same length")
        
        query = """
        UNWIND $mappings AS mapping
        MATCH (c:Chunk {chunk_id: mapping.chunk_id})
        SET c.qdrant_id = mapping.qdrant_id
        """
        
        mappings = [{"chunk_id": chunk_id, "qdrant_id": qdrant_id} 
                   for chunk_id, qdrant_id in zip(chunk_ids, qdrant_ids)]
        
        with self.driver.session(database=self.database) as session:
            try:
                session.run(query, mappings=mappings)
                logger.info(f"Linked {len(mappings)} chunks to Qdrant points")
            except Exception as e:
                logger.error(f"Error linking chunks to Qdrant: {str(e)}")
                raise
    
    def get_document_chunks(self, document_id: str) -> List[Dict[str, Any]]:
        """
        Get all chunks for a specific document.
        
        Args:
            document_id: Document ID
            
        Returns:
            List of dictionaries containing chunk data
        """
        query = """
        MATCH (d:Document {document_id: $document_id})-[:CONTAINS]->(c:Chunk)
        RETURN c.chunk_id AS chunk_id, c.text AS text, 
               properties(c) AS metadata, c.qdrant_id AS qdrant_id
        """
        
        with self.driver.session(database=self.database) as session:
            try:
                result = session.run(query, document_id=document_id)
                chunks = []
                for record in result:
                    chunk_data = {
                        "chunk_id": record["chunk_id"],
                        "text": record["text"],
                        "metadata": record["metadata"],
                        "qdrant_id": record["qdrant_id"]
                    }
                    chunks.append(chunk_data)
                
                logger.info(f"Retrieved {len(chunks)} chunks for document: {document_id}")
                return chunks
            except Exception as e:
                logger.error(f"Error retrieving chunks for document: {str(e)}")
                raise
    
    def delete_document(self, document_id: str) -> bool:
        """
        Delete a document and all its related nodes.
        
        Args:
            document_id: Document ID
            
        Returns:
            bool: True if successful
        """
        query = """
        MATCH (d:Document {document_id: $document_id})
        OPTIONAL MATCH (d)-[:CONTAINS]->(c:Chunk)
        OPTIONAL MATCH (d)-[:HAS_HEADER]->(h:Header)
        DETACH DELETE c, h, d
        """
        
        with self.driver.session(database=self.database) as session:
            try:
                session.run(query, document_id=document_id)
                logger.info(f"Deleted document with ID: {document_id}")
                return True
            except Exception as e:
                logger.error(f"Error deleting document: {str(e)}")
                raise
    
    def execute_query(self, query: str, params: Dict[str, Any] = None) -> Result:
        """
        Execute a custom Cypher query.
        
        Args:
            query: Cypher query string
            params: Query parameters
            
        Returns:
            Neo4j Result object
        """
        params = params or {}
        
        with self.driver.session(database=self.database) as session:
            try:
                return session.run(query, **params)
            except Exception as e:
                logger.error(f"Error executing query: {str(e)}")
                raise

# Factory function to get Neo4j client
def get_neo4j_client() -> Neo4jClient:
    """
    Factory method to get a Neo4j client instance.
    
    Returns:
        Neo4jClient instance
    """
    return Neo4jClient()

# Example usage
if __name__ == "__main__":
    # Create a Neo4j client
    client = get_neo4j_client()
    
    try:
        # Create a test document
        doc_metadata = {
            "filename": "test_doc.md",
            "title": "Test Document",
            "created_at": "2023-01-01T00:00:00Z"
        }
        
        document_id = client.create_document(doc_metadata)
        print(f"Created document with ID: {document_id}")
        
        # Create some test chunks
        for i in range(3):
            chunk_text = f"This is test chunk {i+1}."
            chunk_metadata = {
                "header_title": f"Section {i+1}",
                "header_level": 2,
                "position": i
            }
            chunk_id = client.create_chunk(chunk_text, chunk_metadata, document_id)
            print(f"Created chunk with ID: {chunk_id}")
        
        # Retrieve and display chunks
        chunks = client.get_document_chunks(document_id)
        print(f"Retrieved {len(chunks)} chunks:")
        for chunk in chunks:
            print(f"  - {chunk['chunk_id']}: {chunk['text']}")
        
        # Clean up
        client.delete_document(document_id)
        print(f"Deleted document with ID: {document_id}")
    
    finally:
        # Close connection
        client.close() 