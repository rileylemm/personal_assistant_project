import json
import threading
import redis
import logging
from typing import Dict, Any, Callable, List, Optional
import sys
import signal
import time

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
        self.redis_client = None
        self.pubsub = None
        self.channels = Config.REDIS.CHANNELS
        self.subscribers = {}
        self.running = False
        self.listener_thread = None
        self.connect_to_redis()
    
    def connect_to_redis(self):
        """Connect to Redis with retry logic"""
        max_retries = 5
        retry_delay = 1  # seconds
        
        for attempt in range(max_retries):
            try:
                logger.info(f"Connecting to Redis (attempt {attempt+1}/{max_retries})...")
                self.redis_client = redis.Redis(
                    host=Config.REDIS.HOST,
                    port=Config.REDIS.PORT,
                    db=Config.REDIS.DB,
                    decode_responses=True,  # Automatically decode to strings
                    socket_connect_timeout=5,
                    socket_timeout=5,
                    retry_on_timeout=True
                )
                # Test the connection
                self.redis_client.ping()
                
                # Initialize pubsub
                self.pubsub = self.redis_client.pubsub()
                
                logger.info("Successfully connected to Redis")
                return True
            except redis.ConnectionError as e:
                logger.error(f"Redis connection error (attempt {attempt+1}): {str(e)}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
            except Exception as e:
                logger.error(f"Unexpected error connecting to Redis: {str(e)}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
        
        logger.error(f"Failed to connect to Redis after {max_retries} attempts")
        # Initialize a dummy Redis client for graceful degradation
        self.redis_client = DummyRedisClient()
        self.pubsub = DummyPubSub()
        return False
    
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
            # Check connection and reconnect if needed
            if not self._ensure_connection():
                return False
                
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
            # Check connection and reconnect if needed
            if not self._ensure_connection():
                return False
                
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
            if channels_to_subscribe:
                self.pubsub.subscribe(*channels_to_subscribe)
                logger.info(f"Subscribed to channels: {channels_to_subscribe}")
            return True
        except Exception as e:
            logger.error(f"Failed to subscribe to events: {str(e)}")
            return False
    
    def _ensure_connection(self) -> bool:
        """Ensure Redis connection is active, reconnect if needed"""
        try:
            if isinstance(self.redis_client, DummyRedisClient):
                # Try to reconnect if we're using the dummy client
                return self.connect_to_redis()
                
            # Ping to check connection
            self.redis_client.ping()
            return True
        except (redis.ConnectionError, redis.TimeoutError):
            logger.warning("Redis connection lost, attempting to reconnect...")
            return self.connect_to_redis()
        except Exception as e:
            logger.error(f"Unexpected Redis error: {str(e)}")
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
        reconnect_delay = 1  # Initial reconnect delay in seconds
        max_reconnect_delay = 30  # Maximum reconnect delay
        
        while self.running:
            try:
                if not self._ensure_connection():
                    logger.warning("Redis connection unavailable, retrying in {reconnect_delay}s...")
                    time.sleep(reconnect_delay)
                    reconnect_delay = min(reconnect_delay * 2, max_reconnect_delay)  # Exponential backoff
                    continue
                
                # Reset reconnect delay on successful connection
                reconnect_delay = 1
                
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
            except redis.RedisError as e:
                logger.error(f"Redis error in event listener: {str(e)}")
                time.sleep(reconnect_delay)
                reconnect_delay = min(reconnect_delay * 2, max_reconnect_delay)
            except Exception as e:
                logger.error(f"Error in event listener: {str(e)}")
                # Brief pause to prevent CPU spinning on continuous errors
                time.sleep(0.1)


class DummyRedisClient:
    """Dummy Redis client for graceful degradation when Redis is unavailable"""
    def __init__(self):
        self.data = {}
        logger.warning("Using DummyRedisClient - Redis functionality will be limited")
    
    def publish(self, channel, message):
        logger.debug(f"DummyRedisClient: Would publish to {channel}: {message}")
        return 0
    
    def set(self, key, value):
        self.data[key] = value
        logger.debug(f"DummyRedisClient: Set {key}")
        return True
    
    def get(self, key):
        value = self.data.get(key)
        logger.debug(f"DummyRedisClient: Get {key}")
        return value
    
    def keys(self, pattern):
        # Very basic pattern matching, just for document:*:events
        if pattern == 'document:*:events':
            return [k for k in self.data.keys() if k.startswith('document:') and k.endswith(':events')]
        return []
    
    def ping(self):
        return True
    
    def pubsub(self):
        return DummyPubSub()


class DummyPubSub:
    """Dummy PubSub for graceful degradation when Redis is unavailable"""
    def __init__(self):
        logger.warning("Using DummyPubSub - Subscription functionality will be limited")
    
    def subscribe(self, *channels):
        logger.debug(f"DummyPubSub: Would subscribe to {channels}")
        pass
    
    def get_message(self, ignore_subscribe_messages=True, timeout=1.0):
        time.sleep(0.1)  # To prevent CPU spinning
        return None


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