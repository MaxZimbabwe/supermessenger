# my_flask_app/app/__init__.py

from flask import Flask
from .config import Config
from .routes.webhook import webhook_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(webhook_bp)

    return app
