from marshmallow import Schema, fields, validate

class StoreRules(Schema):
    idusuario = fields.Int(required=True)
    questao = fields.Str(required=True, validate=validate.Length(min=1))
    resposta = fields.Str(required=True, validate=validate.Length(min=1))
    
class UpdateRules(Schema):
    id = fields.Int(required=True)
    idstatus = fields.Int(required=False)
    resposta = fields.Str(required=False)
        
class SearchRules(Schema):
    idusuario = fields.Int(required=True)
    idstatus = fields.Int(required=False)

class SearchColaradoresRules(Schema):
    idusuariocolaborador = fields.Int(required=True)
    status = fields.Int(required=True)