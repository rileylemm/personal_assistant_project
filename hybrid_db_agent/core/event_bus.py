import json
import threading
import redis
import logging
from typing import Dict, Any, Callable, List, Optional
import sys
import signal

# Add parent directory to path to import config
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('event_bus')

class EventBus:
    """
    EventBus implementation using Redis pub/sub for event-driven communication.
    """
    def __init__(self):
        """Initialize the Redis connection for the event bus."""
        self.redis_client = redis.Redis(
            host=Config.REDIS.HOST,
            port=Config.REDIS.PORT,
            db=Config.REDIS.DB,
            decode_responses=True  # Automatically decode to strings
        )
        self.pubsub = self.redis_client.pubsub()
        self.channels = Config.REDIS.CHANNELS
        self.subscribers = {}
        self.running = False
        self.listener_thread = None
    
    def publish(self, event_type: str, data: Dict[str, Any]) -> bool:
        """
        Publish an event to the specified channel.
        
        Args:
            event_type: Type of event (must be in Config.REDIS.CHANNELS)
            data: Dictionary containing event data
            
        Returns:
            bool: True if published successfully, False otherwise
        """
        if event_type not in self.channels:
            logger.error(f"Unknown event type: {event_type}")
            return False
        
        channel = self.channels[event_type]
        try:
            # Convert data to JSON string
            message = json.dumps(data)
            self.redis_client.publish(channel, message)
            logger.info(f"Published event {event_type} to {channel}")
            return True
        except Exception as e:
            logger.error(f"Failed to publish event {event_type}: {str(e)}")
            return False
    
    def subscribe(self, event_types: List[str], callback: Callable[[str, Dict[str, Any]], None]) -> bool:
        """
        Subscribe to one or more event types.
        
        Args:
            event_types: List of event types to subscribe to
            callback: Function to call when an event is received
            
        Returns:
            bool: True if subscribed successfully, False otherwise
        """
        try:
            channels_to_subscribe = []
            for event_type in event_types:
                if event_type not in self.channels:
                    logger.error(f"Unknown event type: {event_type}")
                    return False
                channel = self.channels[event_type]
                channels_to_subscribe.append(channel)
                
                # Store the callback for this channel
                if channel not in self.subscribers:
                    self.subscribers[channel] = []
                self.subscribers[channel].append(callback)
            
            # Subscribe to the channels
            self.pubsub.subscribe(*channels_to_subscribe)
            logger.info(f"Subscribed to channels: {channels_to_subscribe}")
            return True
        except Exception as e:
            logger.error(f"Failed to subscribe to events: {str(e)}")
            return False
    
    def start_listening(self) -> None:
        """Start the background thread that listens for events."""
        if self.running:
            logger.warning("Event listener is already running")
            return
        
        self.running = True
        self.listener_thread = threading.Thread(target=self._listen_for_events)
        self.listener_thread.daemon = True
        self.listener_thread.start()
        logger.info("Started event listener thread")
    
    def stop_listening(self) -> None:
        """Stop the background thread that listens for events."""
        if not self.running:
            logger.warning("Event listener is not running")
            return
        
        self.running = False
        if self.listener_thread:
            self.listener_thread.join(timeout=1.0)
            logger.info("Stopped event listener thread")
    
    def _listen_for_events(self) -> None:
        """Background thread function that listens for events."""
        while self.running:
            try:
                message = self.pubsub.get_message(ignore_subscribe_messages=True, timeout=1.0)
                if message is not None:
                    channel = message['channel']
                    data = json.loads(message['data']) if message['data'] else {}
                    
                    # Find the event_type from the channel
                    event_type = None
                    for event, chan in self.channels.items():
                        if chan == channel:
                            event_type = event
                            break
                    
                    if channel in self.subscribers:
                        for callback in self.subscribers[channel]:
                            try:
                                callback(event_type, data)
                            except Exception as e:
                                logger.error(f"Error in event handler for {channel}: {str(e)}")
            except Exception as e:
                logger.error(f"Error in event listener: {str(e)}")
                # Brief pause to prevent CPU spinning on continuous errors
                import time
                time.sleep(0.1)

# Singleton instance
_event_bus_instance = None

def get_event_bus() -> EventBus:
    """
    Get the singleton EventBus instance.
    
    Returns:
        EventBus: The singleton instance
    """
    global _event_bus_instance
    if _event_bus_instance is None:
        _event_bus_instance = EventBus()
    return _event_bus_instance

# Example usage for a worker process
if __name__ == "__main__":
    # Example of how to use the event bus in a worker process
    event_bus = get_event_bus()
    
    def handle_document_uploaded(event_type, data):
        print(f"Received document uploaded event: {data}")
        # Process the document
        document_id = data.get('document_id')
        if document_id:
            # Publish a new event after processing
            event_bus.publish('document_processing_started', {
                'document_id': document_id,
                'timestamp': data.get('timestamp')
            })
    
    # Subscribe to events
    event_bus.subscribe(['document_uploaded'], handle_document_uploaded)
    
    # Start listening for events
    event_bus.start_listening()
    
    # Handle graceful shutdown
    def signal_handler(sig, frame):
        print("Shutting down...")
        event_bus.stop_listening()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    print("Worker started, waiting for events. Press Ctrl+C to exit.")
    
    # Keep the main thread alive
    try:
        signal.pause()
    except KeyboardInterrupt:
        pass 