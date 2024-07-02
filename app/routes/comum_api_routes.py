from flask import Blueprint, request
from marshmallow import ValidationError
from ..services.products.produtcs_moderation_services import ProductsModerationServices
from .rules.products_moderation_rules import StoreProductsRules, SearchProductsRules, UpdateProductsRules
from .strategy_response import bad_validation, create_response, bad_request

api = Blueprint('products', __name__)

rule_store = StoreProductsRules()
rule_search = SearchProductsRules()
rule_update = UpdateProductsRules()

@api.route("/products", methods=['POST'])
def products():
    try:
        rule_store.load(request.args)
    except ValidationError as error:
        return bad_validation(error=error)
    try:
        products_m = ProductsModerationServices()
        result = products_m.store(request.args)
        return create_response({'status': 'success'},message=result,status=201)    
    except Exception as e:
        return bad_request(e)
    

@api.route("/products", methods=['PATCH'])
def products():
    try:
        rule_update.load(request.args)
    except ValidationError as error:
        return bad_validation(error=error)
    
    try:
        products_m = ProductsModerationServices()
        result = products_m.update(request.args)
        return create_response({'status': 'success'},message=result,status=201)    
    except Exception as e:
        return bad_request(e)

@api.route("/products", methods=['GET'])
def products():
    try:
        rule_search.load(request.args)
    except ValidationError as error:
        return bad_validation(error=error)
    
    try:
        products_m = ProductsModerationServices()
        result = products_m.search(request.args)
        return create_response(result,message="",status=201)    
    except Exception as e:
        return bad_request(e)