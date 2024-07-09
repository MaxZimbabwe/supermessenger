from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.usuarios import Usuarios

class UsuariosModeracaoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuarios
        load_instance = True
        include_relationships = False