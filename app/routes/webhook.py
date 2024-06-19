# my_flask_app/app/routes/webhook.py

from flask import Blueprint, request, jsonify
from ..services.chatgpt_service import get_answer_from_chatgpt
from ..services.mercado_libre_service import send_answer_to_mercadolibre

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = data.get('topic')
    
    if event_type == 'questions':
        question_data = data.get('resource')
        handle_question(question_data)
    
    return jsonify({'status': 'success'}), 200

def handle_question(question_data):
    question_text = get_question_text_from_resource(question_data)
    answer = get_answer_from_chatgpt(question_text)
    send_answer_to_mercadolibre(question_data, answer)

def get_question_text_from_resource(resource):
    # Extract the question text from the resource data
    return "Extracted question text"
