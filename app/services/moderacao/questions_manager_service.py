from ...extension import db
from ...models.moderacao import Moderacao
from ...models.moderacao_status import ModeracaoStatus
from ...models.colaboradores import Colaboradores
from ...models.usuarios import Usuarios
from sqlalchemy.orm import joinedload
from ...utils.Filter_params_field_models import FilterParamsFieldModels

class QuestionsManager:

    filterParams: FilterParamsFieldModels
    def __init__(self) -> None:
        self.filterParams = FilterParamsFieldModels()
    
    def store(self, data: dict):
        try:
            moderacao = Moderacao(
                idusuario=data.get('idusuario'),
                idsubject=data.get('idsubject'),
                questao=data.get('questao'),
                resposta=data.get('resposta'),
                idstatus=data.get('idstatus')
            )
            db.session.add(moderacao)
            db.session.commit()
            return {'status': 'success', 'message': 'Question stored successfully'}
        except Exception as e:
            db.session.rollback()
            return {'status': 'error', 'message': str(e)}

    def update(self, data: dict):
        try:
            moderacao = Moderacao.query.get(data.get('id'))
            if not moderacao:
                return {'status': 'error', 'message': 'Question not found'}
            
            moderacao.idusuario = data.get('idusuario', moderacao.idusuario)
            moderacao.questao = data.get('questao', moderacao.questao)
            moderacao.resposta = data.get('resposta', moderacao.resposta)
            moderacao.idstatus = data.get('idstatus', moderacao.idstatus)
            
            db.session.commit()
            return {'status': 'success', 'message': 'Question updated successfully'}
        except Exception as e:
            db.session.rollback()
            return {'status': 'error', 'message': str(e)}
        
    def search(self, params: dict) -> list:
        try:
            query = Moderacao.query.options(joinedload(Moderacao.status))
            filters = self.filterParams.filter_format(Moderacao, params)
            for condition in filters:
                query = query.filter(condition)
            results = self.filterParams.filter_return(query.all())
            return results
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
        
    def colaboracoes(self, params: dict):
        try:
            query = Colaboradores.query.options(joinedload(Usuarios.idusuario))
            filters = self.filterParams.filter_format(Colaboradores, params)
            for condition in filters:
                query = query.filter(condition)
            results = query.all()
            return {'status': 'success', 'data': results}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}