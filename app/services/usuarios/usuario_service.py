from ...models.userapi import Userapp
from ...extension import db
from ...models.integracao import Integracao

class UsuarioService:

    def get_fcem_token(self, idusuario: int) -> str:
        query = db.session.query(Userapp).filter(Userapp.idusuarioapp==idusuario).first()
        return query.fcm_token if query else ''
    
    def get_code_ml(self, idusuario: int):
        query = db.session.query(Integracao).filter(Integracao.idusuario==idusuario).first()
        return query.code if query else ''


