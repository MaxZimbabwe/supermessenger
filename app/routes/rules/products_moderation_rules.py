from marshmallow import Schema, fields, validate

class StoreProductsRules(Schema):

    idusuario = fields.Int(required=True)
    idproexterno = fields.Str(required=True, validate=validate.Length(min=1))
    titulo = fields.Str(required=True, validate=validate.Length(min=1))
    descricao = fields.Str(required=True, validate=validate.Length(min=1))
        
class UpdateProductsRules(Schema):

    idusuario = fields.Int(required=True)
    idproduto = fields.Int(required=True)
        
class SearchProductsRules(Schema):

    idusuario = fields.Int(required=True)
