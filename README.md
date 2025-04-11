# Hybrid Document Database System

A lightweight event-driven system for ingesting, processing, and storing documents in both Neo4j (graph database) and Qdrant (vector database).

## Features

- Upload Markdown (.md) files through a web interface
- Process documents into chunks that respect document structure
- Generate vector embeddings using FastEmbed
- Store document structure in Neo4j graph database
- Store vector embeddings in Qdrant vector database
- Event-driven architecture using Redis pub/sub
- Real-time processing status updates

## Architecture

The system uses an event-driven architecture with the following components:

1. **Flask Web Application**: Provides the user interface for uploading documents and viewing processing status
2. **Event Bus**: Uses Redis pub/sub for communication between components
3. **Document Processor**: Listens for document upload events and coordinates the processing
4. **Chunking Module**: Breaks documents into logical chunks based on content structure
5. **Embedding Module**: Generates vector embeddings for each chunk using FastEmbed
6. **Storage Modules**:
   - Neo4j Client: Stores document structure and relationships
   - Qdrant Client: Stores vector embeddings for semantic search
   - Synchronizer: Coordinates between the two databases

## Prerequisites

- Python 3.8+
- Docker and Docker Compose

## Setup with Docker Compose

### Starting the Database Services

To start both Neo4j and Qdrant:

```bash
docker-compose up -d
```

This will:
- Start Neo4j on port 7474 (browser) and 7687 (bolt)
- Start Qdrant on port 6333 (REST API) and 6334 (gRPC)
- Create persistent data volumes for both services

### Stopping the Services

```bash
docker-compose down
```

### Accessing the Services

- **Neo4j Browser**: http://localhost:7474
  - Default credentials: neo4j/password
  
- **Qdrant API**: http://localhost:6333
  - No authentication by default

## Installation

1. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r hybrid_db_agent/requirements.txt
   ```

3. Configure environment variables (or edit `config.py` directly):
   ```
   # Redis configuration
   export REDIS_HOST=localhost
   export REDIS_PORT=6379
   
   # Neo4j configuration
   export NEO4J_URI=bolt://localhost:7687
   export NEO4J_USER=neo4j
   export NEO4J_PASSWORD=password
   
   # Qdrant configuration
   export QDRANT_URL=http://localhost:6333
   ```

## Running the Application

1. Start the application:
   ```
   cd hybrid_db_agent
   python run.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5001`

3. Upload a markdown file and watch it being processed in real-time

## Command-line Options

The application supports several command-line options:

- `--host`: Host address to run the Flask app on (default: 127.0.0.1)
- `--port`: Port to run the Flask app on (default: 5000)
- `--debug`: Run in debug mode
- `--no-worker`: Do not start the worker process (for development/testing)

Example:
```
python run.py --host 0.0.0.0 --port 8080 --debug
```

## Important Notes

- Both databases must be running for the application to function properly
- Data is persisted in the `./neo4j_data` and `./qdrant_data` directories
- To completely reset the databases, stop the services and delete these directories

## Customizing the Database Setup

Edit the `docker-compose.yml` file to:
- Change port mappings
- Adjust memory allocation
- Modify authentication settings 