from .chatgpt_service import get_answer_from_chatgpt
from .mercado_libre_service import MercadoLivreServices
from .comum_api_services import ComumApiServices

class HandleQuestionsService:

    def __init__(self) -> None:
        pass

    def getTokenMl(self, idusario: int, code: str) -> str:
        api_comum = ComumApiServices()
        api_comum.setTokenAccessComumApi({"default": True})
        token_ml = api_comum.getMercadoLivreToken(idusuario=idusario, code=code)
        return token_ml

    def handle_question(self, question_data: dict):
        idusario = question_data.get('idusuario')
        code = question_data.get('code')
        token_ml = self.getTokenMl(idusario,code)

        ml = MercadoLivreServices()
        ml.set_token_user(token_ml)

        question = ml.get_question_text_from_resource(question_data.get("resource"))
        answer = get_answer_from_chatgpt(question.get("text"))
        ml.send_answer_to_mercadolibre(question_data, answer)
