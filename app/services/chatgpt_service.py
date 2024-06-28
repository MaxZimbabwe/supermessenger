# my_flask_app/app/services/chatgpt_service.py

from openai import OpenAI
from flask import current_app

def get_answer_from_chatgpt(question):
    client = OpenAI(
        api_key=current_app.config['OPENAI_API_KEY'],
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return response['choices'][0]['message']['content'].strip()