import requests
from flask import current_app
from requests.exceptions import HTTPError

class ComumApiServices:

    url = "https://conexaodascompras.com.br/apiapps/api/"
    token = False

    def __init__(self) -> None:
        self.setTokenAccessComumApi()

    def setTokenAccessComumApi(self):
        try:
            login = {"email": current_app.config["API_COMUM_USER"], "password": current_app.config["API_COMUM_PASSWORD"], "idtipointegracao": 2}
            header = self.getHeader()
            response = requests.get(self.url+"usuarios/login", headers=header, params=login)        
            if response.status_code == 200:
                token = response.json()
                self.token = token["success"]["token"]
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

    def getHeader(self) -> dict:
        header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'YourCustomUserAgent'
        }
        return header

    def getHeaderAuth(self) -> dict:
        header = {
            'Authorization': f"Bearer {self.token}",
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'YourCustomUserAgent'
        }
        return header

    def getMercadoLivreToken(self) -> str:
        params = {}
        response = requests.post(self.url+"/login",headers=self.getHeaderAuth(), params=params)        
        if response.status_code == 200:
            token = response.json()
            self.token = token

    def storeAnswers(self) -> None:
        payload = {
            'key1': 'value1',
            'key2': 'value2'
        }
        params = {
            'param1': 'value1',
            'param2': 'value2'
        }

        response = requests.post(self.url+"/", headers=self.getHeaderAuth(), json=payload, params=params)
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Failed to post data: {response.status_code}")