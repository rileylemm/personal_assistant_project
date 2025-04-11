import logging
import os
import sys
from typing import List, Dict, Any, Union, Optional
import numpy as np

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config
from core.chunking import Chunk

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('embedding')

class EmbeddedChunk:
    """
    Represents a chunk with its text, metadata, and embedding vector.
    """
    def __init__(self, text: str, metadata: Dict[str, Any], embedding: np.ndarray):
        self.text = text
        self.metadata = metadata
        self.embedding = embedding
    
    def __repr__(self):
        return f"EmbeddedChunk(text='{self.text[:50]}...', metadata={self.metadata}, embedding_shape={self.embedding.shape})"

class Embedder:
    """
    Base class for embedding generators.
    """
    def __init__(self):
        pass
    
    def embed_chunks(self, chunks: List[Chunk]) -> List[EmbeddedChunk]:
        """
        Generate embeddings for a list of chunks.
        
        Args:
            chunks: List of chunks to embed
            
        Returns:
            List of EmbeddedChunk objects
        """
        raise NotImplementedError("Subclasses must implement embed_chunks")

class FastEmbedder(Embedder):
    """
    Embedding generator using FastEmbed library.
    """
    def __init__(self, model_name: str = Config.PROCESSING.EMBEDDING_MODEL):
        """
        Initialize FastEmbed embedder.
        
        Args:
            model_name: Name of the FastEmbed model to use
        """
        super().__init__()
        self.model_name = model_name
        self._embedding_model = None
        logger.info(f"Initializing FastEmbedder with model: {model_name}")
    
    @property
    def embedding_model(self):
        """
        Lazy-load the embedding model.
        """
        if self._embedding_model is None:
            try:
                from fastembed import TextEmbedding
                self._embedding_model = TextEmbedding(model_name=self.model_name)
                logger.info(f"Loaded FastEmbed model: {self.model_name}")
            except ImportError:
                logger.error("Failed to import fastembed. Make sure it's installed: pip install 'qdrant-client[fastembed]'")
                raise
            except Exception as e:
                logger.error(f"Failed to load FastEmbed model: {str(e)}")
                raise
        return self._embedding_model
    
    def embed_chunks(self, chunks: List[Chunk]) -> List[EmbeddedChunk]:
        """
        Generate embeddings for a list of chunks using FastEmbed.
        
        Args:
            chunks: List of chunks to embed
            
        Returns:
            List of EmbeddedChunk objects with embeddings
        """
        if not chunks:
            logger.warning("No chunks provided for embedding")
            return []
        
        # Extract the texts from chunks
        texts = [chunk.text for chunk in chunks]
        
        logger.info(f"Generating embeddings for {len(texts)} chunks using FastEmbed")
        
        try:
            # FastEmbed returns a generator, convert to a list of numpy arrays
            embeddings = list(self.embedding_model.embed(texts))
            
            # Create EmbeddedChunk objects
            embedded_chunks = []
            for chunk, embedding in zip(chunks, embeddings):
                embedded_chunk = EmbeddedChunk(
                    text=chunk.text,
                    metadata=chunk.metadata,
                    embedding=embedding
                )
                embedded_chunks.append(embedded_chunk)
            
            logger.info(f"Successfully generated {len(embedded_chunks)} embeddings")
            return embedded_chunks
        
        except Exception as e:
            logger.error(f"Error generating embeddings: {str(e)}")
            raise
    
    def embed_single_text(self, text: str) -> np.ndarray:
        """
        Generate embedding for a single text string.
        
        Args:
            text: Text to embed
            
        Returns:
            Numpy array embedding
        """
        try:
            embeddings = list(self.embedding_model.embed([text]))
            return embeddings[0]
        except Exception as e:
            logger.error(f"Error generating embedding for single text: {str(e)}")
            raise

# Factory function to get the appropriate embedder
def get_embedder(embedder_type: str = "fastembed") -> Embedder:
    """
    Factory method to get an embedder instance.
    
    Args:
        embedder_type: Type of embedder to use
        
    Returns:
        Embedder instance
    """
    if embedder_type.lower() == "fastembed":
        return FastEmbedder()
    else:
        raise ValueError(f"Unknown embedder type: {embedder_type}")

# Example usage
if __name__ == "__main__":
    from chunking import MarkdownChunker
    
    # Test with a sample markdown document
    sample_md = """# Test Document
    
This is a test document that we'll use to demonstrate the embedding process.

## Section 1

This is the first section of our document.

## Section 2

This is the second section of our document.
"""
    
    # First, chunk the document
    chunker = MarkdownChunker()
    chunks = chunker.chunk_document(sample_md, {'document_id': 'test-doc', 'filename': 'test.md'})
    
    # Then, generate embeddings
    embedder = get_embedder()
    embedded_chunks = embedder.embed_chunks(chunks)
    
    for i, chunk in enumerate(embedded_chunks):
        print(f"Embedded Chunk {i+1}:")
        print(f"  Text: {chunk.text[:50]}...")
        print(f"  Embedding shape: {chunk.embedding.shape}")
        print() 