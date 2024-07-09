from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.moderacao_status import ModeracaoStatus

class ModeracaoStatusSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ModeracaoStatus
        load_instance = True