import os
import sys
import uuid
from datetime import datetime
from flask import (
    Blueprint, flash, redirect, render_template, request, 
    url_for, jsonify, current_app, Response, stream_with_context
)
from werkzeug.utils import secure_filename
import json
import time
import logging
from threading import Thread

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config
from core.event_bus import get_event_bus

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('flask_routes')

# Create Blueprint
bp = Blueprint('main', __name__)

# Event bus instance
event_bus = get_event_bus()

# Get Redis client from event bus
redis_client = event_bus.redis_client

# Event tracking for SSE (cache in memory for performance, but backed by Redis)
document_events = {}

# Load existing document events from Redis on startup
def load_document_events_from_redis():
    try:
        # Get all document keys
        document_keys = redis_client.keys('document:*:events')
        
        for key in document_keys:
            document_id = key.split(':')[1]
            events_json = redis_client.get(key)
            
            if events_json:
                document_events[document_id] = json.loads(events_json)
                logger.info(f"Loaded {len(document_events[document_id])} events for document {document_id} from Redis")
    except Exception as e:
        logger.error(f"Error loading document events from Redis: {str(e)}")

# Event listener for SSE updates
def setup_event_listeners():
    def handle_event(event_type, data):
        document_id = data.get('document_id')
        if document_id:
            if document_id not in document_events:
                document_events[document_id] = []
            
            # Create new event
            new_event = {
                'type': event_type,
                'data': data,
                'timestamp': data.get('timestamp', datetime.now().isoformat())
            }
            
            # Add event to document events (in-memory cache)
            document_events[document_id].append(new_event)
            
            # Limit the number of events stored
            if len(document_events[document_id]) > 100:
                document_events[document_id] = document_events[document_id][-100:]
            
            # Store events in Redis for persistence
            try:
                redis_key = f"document:{document_id}:events"
                redis_client.set(redis_key, json.dumps(document_events[document_id]))
                logger.debug(f"Stored events for document {document_id} in Redis")
            except Exception as e:
                logger.error(f"Error storing document events in Redis: {str(e)}")
    
    # Subscribe to all relevant events
    event_bus.subscribe([
        'document_uploaded',
        'document_processing_started',
        'document_chunked',
        'embeddings_generated',
        'storage_completed',
        'processing_error'
    ], handle_event)
    
    # Start listening in background
    event_bus.start_listening()
    logger.info("Event listeners set up for SSE")

# Initialize event listeners and load existing events
def init_app_events():
    # Load existing events from Redis
    load_document_events_from_redis()
    
    # Set up event listeners
    setup_event_listeners()

# Helper functions
def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.FLASK.ALLOWED_EXTENSIONS

# Routes
@bp.route('/')
def index():
    """Main page with file upload."""
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload_file():
    """Handle document upload."""
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        # Secure the filename
        filename = secure_filename(file.filename)
        
        # Generate a unique document ID
        document_id = str(uuid.uuid4())
        
        # Create directory for document
        doc_dir = os.path.join(Config.FLASK.UPLOAD_FOLDER, document_id)
        os.makedirs(doc_dir, exist_ok=True)
        
        # Save the file
        filepath = os.path.join(doc_dir, filename)
        file.save(filepath)
        
        # Prepare metadata
        metadata = {
            'document_id': document_id,
            'filename': filename,
            'original_filename': file.filename,
            'filepath': filepath,
            'uploaded_at': datetime.now().isoformat(),
            'file_size': os.path.getsize(filepath)
        }
        
        # Publish document uploaded event
        event_bus.publish('document_uploaded', metadata)
        
        # Redirect to status page
        return redirect(url_for('main.document_status', document_id=document_id))
    
    flash('File type not allowed. Please upload a markdown (.md) file.')
    return redirect(url_for('main.index'))

@bp.route('/status/<document_id>')
def document_status(document_id):
    """Document processing status page."""
    # Check if document exists
    if document_id not in document_events and not os.path.exists(os.path.join(Config.FLASK.UPLOAD_FOLDER, document_id)):
        flash('Document not found')
        return redirect(url_for('main.index'))
    
    return render_template('status.html', document_id=document_id)

@bp.route('/api/status/<document_id>')
def api_document_status(document_id):
    """API endpoint for document status."""
    events = document_events.get(document_id, [])
    
    # Get the latest status
    status = "Unknown"
    if events:
        latest_event = events[-1]
        if latest_event['type'] == 'storage_completed':
            status = "Completed"
        elif latest_event['type'] == 'processing_error':
            status = "Error"
        elif latest_event['type'] == 'embeddings_generated':
            status = "Storing"
        elif latest_event['type'] == 'document_chunked':
            status = "Embedding"
        elif latest_event['type'] == 'document_processing_started':
            status = "Chunking"
        elif latest_event['type'] == 'document_uploaded':
            status = "Uploaded"
    
    return jsonify({
        'document_id': document_id,
        'status': status,
        'events': events
    })

@bp.route('/api/events/<document_id>')
def api_document_events(document_id):
    """SSE endpoint for document events."""
    def generate():
        # Return any existing events first
        if document_id in document_events:
            yield f"data: {json.dumps({'events': document_events[document_id]})}\n\n"
        
        # Then listen for new events
        last_event_count = len(document_events.get(document_id, []))
        while True:
            current_events = document_events.get(document_id, [])
            current_count = len(current_events)
            
            if current_count > last_event_count:
                # New events, send them
                new_events = current_events[last_event_count:]
                yield f"data: {json.dumps({'events': new_events})}\n\n"
                last_event_count = current_count
            
            # Check if processing is complete or failed
            if current_events and current_events[-1]['type'] in ('storage_completed', 'processing_error'):
                # Final event reached, close the connection
                break
            
            time.sleep(0.5)  # Throttle
    
    return Response(stream_with_context(generate()), 
                   mimetype='text/event-stream',
                   headers={'Cache-Control': 'no-cache', 
                           'Connection': 'keep-alive'})

@bp.route('/documents')
def document_list():
    """List all processed documents."""
    # Ensure we have the latest documents from Redis
    load_document_events_from_redis()
    
    # Collect all document IDs we have events for
    all_documents = []
    
    # From events
    for doc_id, events in document_events.items():
        if events:  # If we have events for this document
            latest_event = events[-1]
            doc_info = {
                'document_id': doc_id,
                'status': 'Unknown',
                'filename': None,
                'uploaded_at': None
            }
            
            # Find upload metadata
            for event in events:
                if event['type'] == 'document_uploaded':
                    doc_info['filename'] = event['data'].get('filename')
                    doc_info['uploaded_at'] = event['data'].get('uploaded_at')
                    break
            
            # Determine status from latest event
            if latest_event['type'] == 'storage_completed':
                doc_info['status'] = "Completed"
            elif latest_event['type'] == 'processing_error':
                doc_info['status'] = "Error"
            elif latest_event['type'] == 'embeddings_generated':
                doc_info['status'] = "Storing"
            elif latest_event['type'] == 'document_chunked':
                doc_info['status'] = "Embedding"
            elif latest_event['type'] == 'document_processing_started':
                doc_info['status'] = "Chunking"
            elif latest_event['type'] == 'document_uploaded':
                doc_info['status'] = "Uploaded"
            
            all_documents.append(doc_info)
    
    # Sort by uploaded_at (most recent first)
    all_documents.sort(key=lambda x: x.get('uploaded_at') or '', reverse=True)
    
    return render_template('documents.html', documents=all_documents)

@bp.route('/api/search', methods=['POST'])
def api_search():
    """API endpoint for semantic search."""
    # This would normally use the Qdrant/Neo4j client to search
    # For demo purposes, we'll just return a dummy response
    return jsonify({
        'status': 'error',
        'message': 'Search functionality not implemented in the demo'
    }) 