from app.services.microservices.comum_api_service import ComumApiServices

def testeSetTokenAccessComumApi(api_comum: ComumApiServices):
    assert isinstance(api_comum.token, str)