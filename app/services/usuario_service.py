from ..models.userapi import Userapp
from ..models.usuario import Usuario
from ..extension import db

class UsuarioService:

    def get_fcem_token(self, idusuario: int) -> str:
        query = db.session.query(Userapp).filter(Userapp.idusuarioapp==idusuario).first()
        return query.fcm_token if query else ''