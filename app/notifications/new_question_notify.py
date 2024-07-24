import requests
from flask import current_app

class NewQuestionNotify:
    @staticmethod
    def send_push_notification(token: str, title: str, body: str, metadata = {}):        
        
        expo_push_token = token
        #expo_access_token = current_app.config['EXPO_ACCESS_KEY']

        notification_data = {
            "to": expo_push_token,
            "sound": "default",
            "title": title,
            "body": body,
            "data": metadata
        }

        url = "https://api.expo.dev/v2/push/send"
        headers = {
            "Content-Type": "application/json",
            #"Authorization": f"Bearer {expo_access_token}"
        }

        response = requests.post(url, headers=headers, json=notification_data)

        if response.status_code == 200:
            return True
        else:
            raise(f"Error sending notification: {response.text}")