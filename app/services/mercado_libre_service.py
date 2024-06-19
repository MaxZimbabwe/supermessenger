# my_flask_app/app/services/mercado_libre_service.py

import requests
from flask import current_app

def send_answer_to_mercadolibre(question_data, answer):
    question_id = question_data['id']
    access_token = current_app.config['MERCADO_LIBRE_ACCESS_TOKEN']
    url = f"https://api.mercadolibre.com/answers?access_token={access_token}"
    
    payload = {
        "question_id": question_id,
        "text": answer
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Answer successfully sent to Mercado Libre")
    else:
        print("Failed to send answer to Mercado Libre", response.text)
