from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from app.services.authentication_service import AuthenticationService

authentication_bp = Blueprint('authentication', __name__)

@authentication_bp.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    password = request.json['password']

    # Call the authentication service to register the user
    success, message = AuthenticationService.register_user(email, password)

    if success:
        return jsonify({'message': message}), 201
    else:
        return jsonify({'message': message}), 400

@authentication_bp.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    # Call the authentication service to authenticate the user
    success, message = AuthenticationService.authenticate_user(email, password)

    if success:
        # Generate access token
        access_token = create_access_token(identity=email)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': message}), 401
