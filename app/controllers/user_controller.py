from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.user_service import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/users/profile', methods=['GET'])
@jwt_required
def get_user_profile():
    user_email = get_jwt_identity()

    # Call the user service to retrieve the user's profile
    user_profile = UserService.get_user_profile(user_email)

    return jsonify(user_profile), 200

@user_bp.route('/users/profile', methods=['PUT'])
@jwt_required
def update_user_profile():
    user_email = get_jwt_identity()
    updated_profile = request.json

    # Call the user service to update the user's profile
    success, message = UserService.update_user_profile(user_email, updated_profile)

    if success:
        return jsonify({'message': message}), 200
    else:
        return jsonify({'message': message}), 400

@user_bp.route('/users/recipes', methods=['GET'])
@jwt_required
def get_user_recipes():
    user_email = get_jwt_identity()

    # Call the user service to retrieve the user's recipes
    user_recipes = UserService.get_user_recipes(user_email)

    return jsonify({'recipes': user_recipes}), 200

@user_bp.route('/users/favorites', methods=['GET'])
@jwt_required
def get_user_favorites():
    user_email = get_jwt_identity()

    # Call the user service to retrieve the user's favorite recipes
    user_favorites = UserService.get_user_favorites(user_email)

    return jsonify({'favorites': user_favorites}), 200
