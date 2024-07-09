from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.moderacao import Moderacao
from .moderacao_status_schema import ModeracaoStatusSchema
from .usuarios_schema import UsuariosSchema
from marshmallow_sqlalchemy.fields import Nested

class ModeracaoSchema(SQLAlchemyAutoSchema):
    status = Nested(ModeracaoStatusSchema)
    usuario = Nested(UsuariosSchema)

    class Meta:
        model = Moderacao
        load_instance = True
        include_relationships = True