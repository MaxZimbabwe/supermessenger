import requests
from flask import current_app
from requests.exceptions import HTTPError
from ..utils.headers import getHeader, getHeaderAuth

class ComumApiServices:

    url = "https://conexaodascompras.com.br/apiapps/api/"
    #url = "http://api.local/apiapps/api/"
    token = False

    def __init__(self) -> None:
        pass

    def setTokenAccessComumApi(self, params: dict):
        try:

            if params.get("default"):
                login = {"email": current_app.config["API_COMUM_USER"], "password": current_app.config["API_COMUM_PASSWORD"], "idtipointegracao": 2}
            else:
                login = params
            
            header = getHeader()
            response = requests.get(self.url+"usuarios/login", headers=header, params=login)        
            if response.status_code == 200:
                token = response.json()
                self.token = token["success"]["token"]
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

    def getMercadoLivreToken(self, idusuario: int, code: str) -> str:
        try:
            params = {"idusuario": idusuario, "code": code}
            response = requests.post(self.url+"integracoes/mercadolivre/autenticacao/token",headers=getHeaderAuth(self.token), params=params)        
            if response.status_code == 200:
                token = response.json()
                return token.get("token")
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")