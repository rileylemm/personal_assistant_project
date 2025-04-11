import logging
import os
import sys
import time
import json
import signal
from datetime import datetime
import uuid
from typing import Dict, Any, List, Optional

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config
from core.event_bus import get_event_bus
from core.chunking import MarkdownChunker
from core.embedding import get_embedder
from storage.sync import get_db_sync

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('processor_worker')

class DocumentProcessor:
    """
    Worker that processes documents through the pipeline.
    """
    def __init__(self):
        """Initialize the document processor."""
        self.event_bus = get_event_bus()
        self.chunker = MarkdownChunker()
        self.embedder = get_embedder()
        self.db_sync = get_db_sync()
        self.running = False
        
        logger.info("Initialized document processor worker")
    
    def start(self):
        """Start listening for document processing events."""
        if self.running:
            logger.warning("Document processor is already running")
            return
        
        # Subscribe to document uploaded events
        self.event_bus.subscribe(
            ['document_uploaded'],
            self._handle_document_uploaded
        )
        
        # Start the event listener
        self.event_bus.start_listening()
        self.running = True
        
        logger.info("Document processor started and listening for events")
    
    def stop(self):
        """Stop the document processor."""
        if not self.running:
            logger.warning("Document processor is not running")
            return
        
        # Stop the event listener
        self.event_bus.stop_listening()
        
        # Close database connections
        self.db_sync.close()
        
        self.running = False
        logger.info("Document processor stopped")
    
    def _handle_document_uploaded(self, event_type: str, data: Dict[str, Any]):
        """
        Handle document uploaded events.
        
        Args:
            event_type: Type of event
            data: Event data containing document information
        """
        logger.info(f"Received {event_type} event: {data}")
        
        try:
            # Extract document info
            document_id = data.get('document_id')
            filepath = data.get('filepath')
            
            if not document_id or not filepath:
                logger.error("Missing document_id or filepath in event data")
                self._publish_error(data, "Missing document information")
                return
            
            # Publish processing started event
            self._publish_processing_started(data)
            
            # Process the document
            self._process_document(document_id, filepath, data)
            
        except Exception as e:
            logger.error(f"Error processing document: {str(e)}")
            self._publish_error(data, str(e))
    
    def _process_document(self, document_id: str, filepath: str, metadata: Dict[str, Any]):
        """
        Process a document through the pipeline.
        
        Args:
            document_id: Document ID
            filepath: Path to the document file
            metadata: Additional document metadata
        """
        try:
            # Step 1: Read the document
            document_text = self._read_document(filepath)
            
            # Add the document content length to metadata
            metadata['content_length'] = len(document_text)
            metadata['processing_started'] = datetime.now().isoformat()
            
            # Step 2: Chunk the document
            chunks = self.chunker.chunk_document(document_text, metadata)
            logger.info(f"Document chunked into {len(chunks)} chunks")
            
            # Publish chunking completed event
            self._publish_document_chunked(document_id, len(chunks))
            
            # Step 3: Generate embeddings
            embedded_chunks = self.embedder.embed_chunks(chunks)
            logger.info(f"Generated embeddings for {len(embedded_chunks)} chunks")
            
            # Publish embeddings generated event
            self._publish_embeddings_generated(document_id, len(embedded_chunks))
            
            # Step 4: Store in databases
            chunk_ids = self.db_sync.store_embedded_chunks(embedded_chunks, document_id)
            logger.info(f"Stored {len(chunk_ids)} chunks in databases")
            
            # Update metadata with processing info
            metadata['chunk_count'] = len(chunks)
            metadata['processed_at'] = datetime.now().isoformat()
            
            # Publish storage completed event
            self._publish_storage_completed(document_id, metadata)
            
        except Exception as e:
            logger.error(f"Error in document processing pipeline: {str(e)}")
            self._publish_error(metadata, str(e))
            raise
    
    def _read_document(self, filepath: str) -> str:
        """
        Read document content from file.
        
        Args:
            filepath: Path to the document file
            
        Returns:
            str: Document content
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            logger.info(f"Read document from {filepath}, size: {len(content)} bytes")
            return content
        except Exception as e:
            logger.error(f"Error reading document file {filepath}: {str(e)}")
            raise
    
    def _publish_processing_started(self, data: Dict[str, Any]):
        """Publish document processing started event."""
        event_data = data.copy()
        event_data['timestamp'] = datetime.now().isoformat()
        self.event_bus.publish('document_processing_started', event_data)
    
    def _publish_document_chunked(self, document_id: str, chunk_count: int):
        """Publish document chunked event."""
        event_data = {
            'document_id': document_id,
            'chunk_count': chunk_count,
            'timestamp': datetime.now().isoformat()
        }
        self.event_bus.publish('document_chunked', event_data)
    
    def _publish_embeddings_generated(self, document_id: str, embedding_count: int):
        """Publish embeddings generated event."""
        event_data = {
            'document_id': document_id,
            'embedding_count': embedding_count,
            'timestamp': datetime.now().isoformat()
        }
        self.event_bus.publish('embeddings_generated', event_data)
    
    def _publish_storage_completed(self, document_id: str, metadata: Dict[str, Any]):
        """Publish storage completed event."""
        event_data = {
            'document_id': document_id,
            'metadata': metadata,
            'timestamp': datetime.now().isoformat()
        }
        self.event_bus.publish('storage_completed', event_data)
    
    def _publish_error(self, data: Dict[str, Any], error_message: str):
        """Publish processing error event."""
        event_data = data.copy()
        event_data['error'] = error_message
        event_data['timestamp'] = datetime.now().isoformat()
        self.event_bus.publish('processing_error', event_data)

def main():
    """Main entry point for the processor worker."""
    processor = DocumentProcessor()
    
    # Handle graceful shutdown
    def signal_handler(sig, frame):
        logger.info("Shutting down document processor...")
        processor.stop()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Start processing
    processor.start()
    
    logger.info("Document processor worker running. Press Ctrl+C to exit.")
    
    # Keep the main thread alive
    try:
        while processor.running:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        processor.stop()

if __name__ == "__main__":
    main() 