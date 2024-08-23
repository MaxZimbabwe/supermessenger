from ...extension import db
from ...models.moderacao import Moderacao
from ...models.moderacao_status import ModeracaoStatus
from ...models.colaboradores import Colaboradores
from ...models.usuarios import Usuarios
from sqlalchemy.orm import joinedload
from ...utils.Filter_params_field_models import FilterParamsFieldModels
from ...schemas.moderacao_schema import ModeracaoSchema
from ...schemas.colaboradores_schema import ColaboradoresSchema
from sqlalchemy import update

moderacao_schema = ModeracaoSchema(many=True)
colaboracao_schema = ColaboradoresSchema(many=True)

class QuestionsManager:

    filterParams: FilterParamsFieldModels
    def __init__(self) -> None:
        self.filterParams = FilterParamsFieldModels()
    
    def store(self, data: dict):
        try:
            moderacao = Moderacao(
                idusuario=data.get('idusuario'),
                idsubject=data.get('idsubject'),
                idresource=data.get('idresource'),
                idpergunta=data.get('idpergunta'),
                titulo=data.get('titulo'),
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

    def update(self, params: dict):
        try:
            db.session.execute(update(Moderacao),[
                params
            ])
            db.session.commit()
            return True
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
        
    def search(self, params: dict) -> list:
        try:
            query = db.session.query(Moderacao).options(
                joinedload(Moderacao.status),
                # Add other relationships you want to load here
            )
            filters = self.filterParams.filter_format(Moderacao, params)
            for condition in filters:
                query = query.filter(condition)
            results = query.all()

            if results:
                data = moderacao_schema.dump(results)
            else:
                data = {}
            return data
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
        
    def colaboracoes(self, params: dict):
        try:
            query = db.session.query(Colaboradores).options(
                joinedload(Colaboradores.colaboradores),
                joinedload(Colaboradores.colaborando),
                # Add other relationships you want to load here
            )
            filters = self.filterParams.filter_format(Colaboradores, params)
            for condition in filters:
                query = query.filter(condition)
            results = query.all()
            if results:
                data = colaboracao_schema.dump(results)
            else:
                data = {}
            return data
        except Exception as e:
            return {'status': 'error', 'message': str(e)}     
    