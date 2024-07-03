from ...extension import db
from ...models.moderacao import Moderacao
from ...models.moderacao_status import ModeracaoStatus
from ...models.colaboradores import Colaboradores
from sqlalchemy.orm import joinedload

class QuestionsManager:
    
    def store(self, data: dict):
        try:
            moderacao = Moderacao(
                idusuario=data.get('idusuario'),
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

    def questions(self, filter: list):
        try:
            query = Moderacao.query.options(joinedload(Moderacao.status))
            for condition in filter:
                query = query.filter(condition)
            results = query.all()
            return {'status': 'success', 'data': results}
        except Exception as e:
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

    def colaboracoes():
        try:
            query = Colaboradores.query.options(joinedload(Colaboradores.usuario_colaborador))
            for condition in filter:
                query = query.filter(condition)
            results = query.all()
            return {'status': 'success', 'data': results}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}