# my_flask_app/app/config.py
from urllib.parse import quote_plus
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    MERCADO_LIBRE_ACCESS_TOKEN = os.getenv('MERCADO_LIBRE_ACCESS_TOKEN')
    API_COMUM_USER=os.getenv('API_COMUM_USER','viinicius-rn@hotmail.com')
    API_COMUM_PASSWORD=os.getenv('API_COMUM_PASSWORD',123)
    password = "dn;k$g34@@TU"
    encoded_password = quote_plus(password)
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://cone0002_apps2:{encoded_password}@69.49.241.106/cone0002_apps'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FIREBASE_SERVER_KEY=os.getenv('FIREBASE_SERVER_KEY', 'default_secret_key')