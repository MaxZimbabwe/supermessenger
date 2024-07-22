from flask import Flask, jsonify
from marshmallow import ValidationError
from ..models.logs import Logs
from ..extension import db
import traceback
from json import JSONDecodeError

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
    # Extracting error information
    error_type = type(error).__name__
    error_description = str(error)

    # Handling JSONDecodeError specifically
    if isinstance(error, JSONDecodeError):
        error_trace = traceback.format_exc()
        error_message = f"JSON Decode Error: {error_description}, Traceback: {error_trace}"
        response_code = 400
    else:
        # Getting full traceback for other exceptions
        error_trace = traceback.format_exc()
        error_message = f"Error type: {error_type}, Description: {error_description}, Traceback: {error_trace}"
        response_code = 500

    # Saving the log into the database
    new_log = Logs(log=error_message)
    db.session.add(new_log)
    db.session.commit()

    return create_response(message=error_message, status='error', code=response_code)

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
