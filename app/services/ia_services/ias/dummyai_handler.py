# my_flask_app/app/services/chatgpt_service.py

import openai
from flask import current_app
from ..handler import Handler

class DummyHandler(Handler):

    def handle(self, subject: str, question: str) -> str:
        return "Dummy response..."