# App package initialization
import os
from flask import Flask

def create_app(test_config=None):
    """Create and configure the Flask application."""
    # Create Flask app
    app = Flask(__name__, instance_relative_config=True)
    
    # Load configuration
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config import Config
    
    app.config.from_mapping(
        SECRET_KEY=Config.FLASK.SECRET_KEY,
        UPLOAD_FOLDER=Config.FLASK.UPLOAD_FOLDER,
        MAX_CONTENT_LENGTH=Config.FLASK.MAX_CONTENT_LENGTH
    )
    
    # Ensure the upload folder exists
    os.makedirs(Config.FLASK.UPLOAD_FOLDER, exist_ok=True)
    
    # Jinja2 datetime filter
    @app.template_filter('datetime')
    def format_datetime(value, format='%Y-%m-%d %H:%M:%S'):
        """Format a datetime object."""
        if value:
            return value
        return ""
    
    # Register blueprints
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app 