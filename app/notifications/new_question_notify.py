import requests
from flask import current_app

class NewQuestionNotify:
    @staticmethod
    def send_push_notification(token, title, body):
        server_key = current_app.config['FIREBASE_SERVER_KEY']
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + server_key,
        }
        payload = {
            'to': token,
            'notification': {
                'title': title,
                'body': body,
            },
        }
        response = requests.post('https://fcm.googleapis.com/fcm/send', headers=headers, json=payload)
        return response.json()