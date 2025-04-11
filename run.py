#!/usr/bin/env python
"""
Main entry point for the Hybrid Document Database application.
This starts the Flask web application.
"""

import os
import sys
import argparse
import logging
from threading import Thread

# Add hybrid_db_agent to the path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('run')

# Start worker process
def start_worker_process(worker_module):
    """Start a worker process in a separate Python process."""
    import subprocess
    
    logger.info(f"Starting worker process: {worker_module}")
    
    # Start the worker as a subprocess
    worker_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hybrid_db_agent', worker_module)
    process = subprocess.Popen([sys.executable, worker_path])
    
    logger.info(f"Worker process started with PID: {process.pid}")
    return process

def main():
    """Main entry point."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Run the Hybrid Document Database application')
    parser.add_argument('--host', default='127.0.0.1', help='Host to run the Flask app on')
    parser.add_argument('--port', type=int, default=5001, help='Port to run the Flask app on')
    parser.add_argument('--debug', action='store_true', help='Run in debug mode')
    parser.add_argument('--no-worker', action='store_true', help='Do not start the worker process')
    args = parser.parse_args()
    
    # Initialize worker process
    worker_process = None
    if not args.no_worker:
        worker_process = start_worker_process('workers/processor_worker.py')
    
    try:
        # Import and run Flask app
        from hybrid_db_agent.app import create_app
        app = create_app()
        
        logger.info(f"Starting Flask app on {args.host}:{args.port}")
        app.run(host=args.host, port=args.port, debug=args.debug)
    
    finally:
        # Terminate worker process on exit
        if worker_process:
            logger.info("Terminating worker process")
            worker_process.terminate()
            worker_process.wait()

if __name__ == '__main__':
    main() 