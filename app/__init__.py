# my_flask_app/app/__init__.py

from flask import Flask
from .config import Config
from .routes.webhook import webhook_bp
from .extension import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():        
        from .models import init_models
        init_models()


    # Register Blueprints
    app.register_blueprint(webhook_bp)

    return app
