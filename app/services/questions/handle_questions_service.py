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
    
    def get_question(self, token_ml: str, resource: str) -> dict:
        mlapi = MercadoLivreServices()
        mlapi.set_token_user(token_ml)
        question = mlapi.get_question_text_from_resource(resource)
        return question

    def handle_question(self, question_data: dict):
        idusario = question_data.get('idusuario')
        code = question_data.get('code')
        token_ml = self.getTokenMl(idusario,code)

        mlapi = MercadoLivreServices()
        mlapi.set_token_user(token_ml)

        question_id = question_data.get("resource").split("/")
        question = self.get_question(token_ml, question_id[-1])
        status = question.get("status")

        if status != 'UNANSWERED':
            items = (question.get("item_id"),)
            subject = mlapi.get_item_details(items)
            ias = ClientIAs()
            answer = ias.question(subject[0]["body"].get("title"), question.get("text"))
            
            title = subject[0]["body"].get("title")
            
            questionmaneger = QuestionsManager()
            questionmaneger.store({"idusuario": idusario, "idpergunta": question_data.get("_id"), "idresource": question_id[-1], "idsubject": question.get("item_id"),"titulo": title, "questao": question.get("text"), "resposta": answer, "idstatus": 1})

            for token in question_data.get('tokens'):
                # Send a notification 
                NewQuestionNotify.send_push_notification(token=token,body=answer,title=title)

    def answer_question(self, params: dict) -> dict:
        usuario = UsuarioService()
        code = usuario.get_code_ml(params.get('idusuario'))
        token_ml = self.getTokenMl(params.get('idusuario'),code)
        question = self.get_question(token_ml=token_ml,resource=params.get("idresource"))
        status = question.get("status")

        if status != 'UNANSWERED':
            mlapi = MercadoLivreServices()
            mlapi.set_token_user(token_ml)
            #mlapi.send_answer_to_mercadolibre(question, params.get("resposta"))            

        moderacao = QuestionsManager()
        moderacao.update(params)

        return {'status_question': status, 'update': True}