from flask import Flask, jsonify
from marshmallow import ValidationError

app = Flask(__name__)

def create_response(data=None, message='', status='success', code=200):
    
    response = {
        'status': status,
        'message': message,
        'data': data,
        'code': code
    }
    return jsonify(response), code

@app.errorhandler(400)
def bad_validation(error: ValidationError):
    return jsonify(error.messages), 422

@app.errorhandler(400)
def bad_request(error):
    # Extraindo informações do erro
    error_description = str(error.description) if hasattr(error, 'description') else 'No description available'

    logs = ''
    if isinstance(error, dict):
        if error.get('args',False):
            list_errors = error.get('args',[])
            logs = ",".join(list_errors)

    error_message = f"Bad request: {error_description} {logs}"
    return create_response(message=error_message, status='error', code=400)

@app.errorhandler(401)
def unauthorized(error):
    return create_response(message="Unauthorized", status='error', code=401)

@app.errorhandler(403)
def forbidden(error):
    return create_response(message="Forbidden", status='error', code=403)

@app.errorhandler(404)
def not_found(error):
    return create_response(message="Not Found", status='error', code=404)

@app.errorhandler(500)
def internal_server_error(error):
    return create_response(message="Internal Server Error", status='error', code=500)
