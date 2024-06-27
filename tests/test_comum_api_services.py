from app.services.comum_api_services import ComumApiServices

def testeSetTokenAccessComumApi(api_comum: ComumApiServices):
    assert isinstance(api_comum.token, str)