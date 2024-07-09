from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.colaboradores import Colaboradores
from .usuarios_moderacoes_schema import UsuariosModeracaoSchema
from marshmallow_sqlalchemy.fields import Nested

class ColaboradoresSchema(SQLAlchemyAutoSchema):
    colaboradores = Nested(UsuariosModeracaoSchema, many=True)
    colaborando = Nested(UsuariosModeracaoSchema, many=True)
    class Meta:
        model = Colaboradores
        load_instance = True
        include_relationships = True
