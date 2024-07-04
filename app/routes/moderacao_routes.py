from flask import Blueprint, request
from marshmallow import ValidationError
from ..services.moderacao.questions_manager_service import QuestionsManager
from .rules.moderacao_rules import SearchColaradoresRules, SearchRules, UpdateRules, StoreRules
from .strategy_response import bad_validation, create_response, bad_request

moderacao_route = Blueprint('moderacao', __name__, url_prefix="/moderacao")

rule_store = StoreRules()
rule_search = SearchRules()
rule_update = UpdateRules()
rule_search_colaboradores = SearchColaradoresRules()

@moderacao_route.route("/questions", methods=['POST'])
def store():
    try:
        rule_store.load(request.args)
    except ValidationError as error:
        return bad_validation(error=error)
    try:
        moderacoes = QuestionsManager()
        result = moderacoes.store(request.args)
        return create_response({'status': 'success'},message=result,status=201)    
    except Exception as e:
        return bad_request(e)

@moderacao_route.route("/questions", methods=['PATCH'])
def update():
    try:
        rule_update.load(request.args)
    except ValidationError as error:
        return bad_validation(error=error)
    
    try:
        moderacoes = QuestionsManager()
        result = moderacoes.update(request.args)
        return create_response({'status': 'success'},message=result,status=201)    
    except Exception as e:
        return bad_request(e)

@moderacao_route.route("/questions", methods=['GET'])
def search():
    try:
        rule_search.load(request.args)
    except ValidationError as error:
        return bad_validation(error=error)
    
    try:
        moderacoes = QuestionsManager()
        result = moderacoes.search(request.args)
        return create_response(result,message="",status=201)    
    except Exception as e:
        return bad_request(e)
    
@moderacao_route.route("/colaboracoes/questions", methods=['GET'])
def search_colaboradores():
    try:
        rule_search_colaboradores.load(request.args)
    except ValidationError as error:
        return bad_validation(error=error)
    
    try:
        moderacoes = QuestionsManager()
        result = moderacoes.colaboracoes(request.args)
        return create_response(result,message="",status=201)    
    except Exception as e:
        return bad_request(e)