import os

# Flask settings
class FlaskConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-for-development-only')
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size
    ALLOWED_EXTENSIONS = {'md'}  # For MVP, only markdown files

# Redis settings (for event bus)
class RedisConfig:
    HOST = os.environ.get('REDIS_HOST', 'localhost')
    PORT = int(os.environ.get('REDIS_PORT', 6379))
    DB = int(os.environ.get('REDIS_DB', 0))
    CHANNELS = {
        'document_uploaded': 'doc:uploaded',
        'document_processing_started': 'doc:processing:started',
        'document_chunked': 'doc:chunked',
        'embeddings_generated': 'doc:embeddings:generated',
        'storage_completed': 'doc:storage:completed',
        'processing_error': 'doc:error'
    }

# Neo4j settings
class Neo4jConfig:
    URI = os.environ.get('NEO4J_URI', 'bolt://localhost:7687')
    USER = os.environ.get('NEO4J_USER', 'neo4j')
    PASSWORD = os.environ.get('NEO4J_PASSWORD', 'password')
    DATABASE = os.environ.get('NEO4J_DATABASE', 'neo4j')

# Qdrant settings
class QdrantConfig:
    URL = os.environ.get('QDRANT_URL', 'http://localhost:6333')
    COLLECTION_NAME = os.environ.get('QDRANT_COLLECTION', 'document_chunks')
    VECTOR_SIZE = 384  # Default for FastEmbed 'BAAI/bge-small-en-v1.5'

# Document processing settings
class ProcessingConfig:
    # Chunking settings
    CHUNK_MIN_SIZE = 100  # Minimum characters per chunk
    CHUNK_MAX_SIZE = 1000  # Maximum characters per chunk
    CHUNK_OVERLAP = 50  # Overlap between chunks
    
    # Embedding settings
    EMBEDDING_MODEL = 'BAAI/bge-small-en-v1.5'  # Default FastEmbed model

# Combine all configs
class Config:
    FLASK = FlaskConfig
    REDIS = RedisConfig
    NEO4J = Neo4jConfig
    QDRANT = QdrantConfig
    PROCESSING = ProcessingConfig 