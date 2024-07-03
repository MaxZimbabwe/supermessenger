# my_flask_app/app/services/mercado_libre_service.py

import requests
from ...routes.strategy_response import create_response, bad_request
from requests.exceptions import HTTPError

class MercadoLivreServices:

    url_ml_api = "https://api.mercadolibre.com"
    token = None

    def __init__(self) -> None:
        pass

    def set_token_user(self, token: str):
        self.token = token

    def send_answer_to_mercadolibre(self, question_data, answer):
        try:
            question_id = question_data.get('_id')
            access_token = self.token
            url = f"https://api.mercadolibre.com/answers?access_token={access_token}"
            
            payload = {
                "question_id": question_id,
                "text": answer
            }
            
            response = requests.post(url, json=payload)            
            return create_response(message="Answer successfully sent to Mercado Libre", data=response)
            
        except HTTPError as http_err:
            return bad_request(http_err)
        except Exception as err:
            return bad_request(err)

    def get_question_text_from_resource(self, resource: str) -> dict:
        try:
            question_id = resource.split("/")
            url = f"https://api.mercadolibre.com/questions/{question_id[-1]}"
            
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                "Authorization": 'Bearer ' + self.token
            }
            
            response = requests.get(url,headers=headers)            
            question = response.json()
            return question
            
        except HTTPError as http_err:
            return bad_request(http_err)
        except Exception as err:
            return bad_request(err)
        
    def get_item_details(self, iditems: tuple) -> dict:
        try:
            url = "https://api.mercadolibre.com/items?ids="+",".join(iditems)
            
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                "Authorization": 'Bearer ' + self.token
            }
            
            response = requests.get(url,headers=headers)            
            question = response.json()
            return question
            
        except HTTPError as http_err:
            return bad_request(http_err)
        except Exception as err:
            return bad_request(err)

