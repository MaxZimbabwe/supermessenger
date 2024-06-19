# my_flask_app/app/services/chatgpt_service.py

import openai
from flask import current_app

def get_answer_from_chatgpt(question):
    openai.api_key = current_app.config['OPENAI_API_KEY']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text.strip()
