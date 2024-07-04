from ..ia_services.cliente_ias import ClientIAs
from ..mercadolivre.mercado_libre_service import MercadoLivreServices
from ..microservices.comum_api_service import ComumApiServices
from ..moderacao.questions_manager_service import QuestionsManager
from ...notifications.new_question_notify import NewQuestionNotify
from ..usuarios.usuario_service import UsuarioService

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

        mlapi = MercadoLivreServices()
        mlapi.set_token_user(token_ml)

        question = mlapi.get_question_text_from_resource(question_data.get("resource"))
        items = (question.get("item_id"),)
        subject = mlapi.get_item_details(items)
        ias = ClientIAs()
        answer = ias.question(subject[0]["body"].get("title"), question.get("text"))

        user = UsuarioService()
        token = user.get_fcem_token(idusario)
        title = subject[0]["body"].get("title")
        
        questionmaneger = QuestionsManager()
        questionmaneger.store({"idusuario": idusario, "idsubject": question.get("item_id"), "questao": title, "resposta": answer, "idstatus": 1})

        # Send a notification 
        NewQuestionNotify.send_push_notification(token=token,body=answer,title=title)