# my_flask_app/app/routes/webhook.py

from flask import Blueprint, request
from ..routes.strategy_response import create_response, bad_request
from ..services.handle_questions_service import HandleQuestionsService

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        event_type = data.get('topic')
        
        if event_type == 'questions':
            questions = HandleQuestionsService()
            questions.handle_question(data)
                    
        return create_response({'status': 'success'},message="",status=201)    
    except Exception as e:
        return bad_request(e)