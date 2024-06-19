# my_flask_app/app/config.py

import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    MERCADO_LIBRE_ACCESS_TOKEN = os.getenv('MERCADO_LIBRE_ACCESS_TOKEN')
