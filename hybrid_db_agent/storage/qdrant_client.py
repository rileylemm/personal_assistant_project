import logging
import os
import sys
from typing import Dict, List, Any, Optional, Union, Tuple
import uuid
import numpy as np

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config

# Import Qdrant client
try:
    from qdrant_client import QdrantClient, AsyncQdrantClient
    from qdrant_client.http.models import (
        Distance,
        VectorParams,
        PointStruct,
        Filter,
        FieldCondition,
        MatchValue,
        SearchRequest
    )
except ImportError:
    logging.error("Qdrant client not installed. Run 'pip install qdrant-client[fastembed]'")
    raise

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('qdrant_client')

class QdrantClientWrapper:
    """
    Wrapper for Qdrant client to store and retrieve vector embeddings.
    """
    def __init__(
        self,
        url: str = Config.QDRANT.URL,
        collection_name: str = Config.QDRANT.COLLECTION_NAME,
        vector_size: int = Config.QDRANT.VECTOR_SIZE
    ):
        """
        Initialize Qdrant client.
        
        Args:
            url: Qdrant server URL
            collection_name: Name of the collection to use
            vector_size: Size of the vector embeddings
        """
        self.url = url
        self.collection_name = collection_name
        self.vector_size = vector_size
        self._client = None
        logger.info(f"Initializing Qdrant client for {url}, collection: {collection_name}")
    
    @property
    def client(self) -> QdrantClient:
        """
        Lazy-load the Qdrant client.
        """
        if self._client is None:
            try:
                self._client = QdrantClient(url=self.url)
                logger.info("Successfully connected to Qdrant")
            except Exception as e:
                logger.error(f"Failed to connect to Qdrant: {str(e)}")
                raise
        return self._client
    
    def create_collection_if_not_exists(self) -> None:
        """
        Create the collection if it doesn't exist.
        """
        try:
            # Check if collection exists
            collections = self.client.get_collections().collections
            collection_names = [collection.name for collection in collections]
            
            if self.collection_name not in collection_names:
                # Create collection
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(
                        size=self.vector_size,
                        distance=Distance.COSINE
                    )
                )
                logger.info(f"Created collection: {self.collection_name}")
            else:
                logger.info(f"Collection {self.collection_name} already exists")
        except Exception as e:
            logger.error(f"Error creating collection: {str(e)}")
            raise
    
    def upsert_points(
        self,
        vectors: List[np.ndarray],
        metadata_list: List[Dict[str, Any]],
        ids: Optional[List[str]] = None
    ) -> List[str]:
        """
        Insert or update points in the collection.
        
        Args:
            vectors: List of vector embeddings
            metadata_list: List of metadata dictionaries
            ids: Optional list of point IDs (generated if not provided)
            
        Returns:
            List of point IDs
        """
        if len(vectors) != len(metadata_list):
            raise ValueError("vectors and metadata_list must have the same length")
        
        if not vectors:
            logger.warning("No vectors provided for upserting")
            return []
        
        # Generate IDs if not provided
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in range(len(vectors))]
        
        # Ensure collection exists
        self.create_collection_if_not_exists()
        
        # Prepare points for upsert
        points = []
        for i, (vec, metadata, point_id) in enumerate(zip(vectors, metadata_list, ids)):
            points.append(
                PointStruct(
                    id=point_id,
                    vector=vec.tolist(),
                    payload=metadata
                )
            )
        
        # Upsert in batches of 100 to avoid overwhelming the server
        batch_size = 100
        for i in range(0, len(points), batch_size):
            batch = points[i:i + batch_size]
            try:
                self.client.upsert(
                    collection_name=self.collection_name,
                    points=batch
                )
                logger.info(f"Upserted batch of {len(batch)} points")
            except Exception as e:
                logger.error(f"Error upserting points: {str(e)}")
                raise
        
        logger.info(f"Successfully upserted {len(points)} points")
        return ids
    
    def search_similar(
        self,
        vector: np.ndarray,
        filter_dict: Optional[Dict[str, Any]] = None,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Search for similar vectors in the collection.
        
        Args:
            vector: Query vector embedding
            filter_dict: Optional filter dictionary
            limit: Maximum number of results
            
        Returns:
            List of dictionaries with search results
        """
        try:
            # Create filter if provided
            filter_obj = None
            if filter_dict:
                conditions = []
                for key, value in filter_dict.items():
                    conditions.append(
                        FieldCondition(
                            key=key,
                            match=MatchValue(value=value)
                        )
                    )
                filter_obj = Filter(must=conditions)
            
            # Search for similar vectors
            results = self.client.search(
                collection_name=self.collection_name,
                query_vector=vector.tolist(),
                query_filter=filter_obj,
                limit=limit
            )
            
            # Process results
            search_results = []
            for result in results:
                search_results.append({
                    "id": result.id,
                    "score": result.score,
                    "payload": result.payload
                })
            
            logger.info(f"Found {len(search_results)} similar vectors")
            return search_results
        
        except Exception as e:
            logger.error(f"Error searching similar vectors: {str(e)}")
            raise
    
    def delete_points(self, ids: List[str]) -> None:
        """
        Delete points from the collection.
        
        Args:
            ids: List of point IDs to delete
        """
        if not ids:
            logger.warning("No IDs provided for deletion")
            return
        
        try:
            self.client.delete(
                collection_name=self.collection_name,
                points_selector=ids
            )
            logger.info(f"Deleted {len(ids)} points")
        except Exception as e:
            logger.error(f"Error deleting points: {str(e)}")
            raise
    
    def delete_points_by_filter(self, filter_dict: Dict[str, Any]) -> None:
        """
        Delete points from the collection by filter.
        
        Args:
            filter_dict: Filter dictionary
        """
        if not filter_dict:
            logger.warning("No filter provided for deletion")
            return
        
        try:
            # Create filter
            conditions = []
            for key, value in filter_dict.items():
                conditions.append(
                    FieldCondition(
                        key=key,
                        match=MatchValue(value=value)
                    )
                )
            filter_obj = Filter(must=conditions)
            
            self.client.delete(
                collection_name=self.collection_name,
                points_selector=filter_obj
            )
            logger.info(f"Deleted points matching filter: {filter_dict}")
        except Exception as e:
            logger.error(f"Error deleting points by filter: {str(e)}")
            raise
    
    def close(self) -> None:
        """
        Close the Qdrant client connection.
        """
        if self._client is not None:
            # No explicit close method in Qdrant client, but we can reset the reference
            self._client = None
            logger.info("Qdrant client reference released")

# Factory function to get Qdrant client
def get_qdrant_client() -> QdrantClientWrapper:
    """
    Factory method to get a Qdrant client instance.
    
    Returns:
        QdrantClientWrapper instance
    """
    return QdrantClientWrapper()

# Example usage
if __name__ == "__main__":
    try:
        # Import FastEmbed for testing
        from fastembed import TextEmbedding
        
        # Create a Qdrant client
        client = get_qdrant_client()
        
        # Create a test embedding
        embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
        texts = [
            "This is a test document for Qdrant.",
            "Another test document with different content."
        ]
        vectors = list(embedding_model.embed(texts))
        
        # Create metadata
        metadata_list = [
            {"text": texts[0], "document_id": "test-doc", "chunk_id": "chunk-1"},
            {"text": texts[1], "document_id": "test-doc", "chunk_id": "chunk-2"}
        ]
        
        # Upsert points
        point_ids = client.upsert_points(vectors, metadata_list)
        print(f"Upserted points with IDs: {point_ids}")
        
        # Search for similar vectors
        query_text = "test document"
        query_vector = list(embedding_model.embed([query_text]))[0]
        results = client.search_similar(query_vector, limit=5)
        
        print(f"Search results for '{query_text}':")
        for i, result in enumerate(results):
            print(f"  {i+1}. ID: {result['id']}")
            print(f"     Score: {result['score']}")
            print(f"     Text: {result['payload'].get('text', 'N/A')}")
        
        # Clean up
        client.delete_points(point_ids)
        print(f"Deleted test points")
        
    except ImportError:
        print("FastEmbed not installed. Run 'pip install qdrant-client[fastembed]'")
    except Exception as e:
        print(f"Error in example: {str(e)}") 