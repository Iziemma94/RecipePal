from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.recipe_service import RecipeService

recipe_bp = Blueprint('recipe', __name__)

@recipe_bp.route('/recipes', methods=['GET'])
def get_recipes():
    # Call the recipe service to retrieve a list of recipes
    recipes = RecipeService.get_recipes()

    return jsonify({'recipes': recipes}), 200

@recipe_bp.route('/recipes', methods=['POST'])
@jwt_required
def create_recipe():
    user_email = get_jwt_identity()
    recipe_data = request.json

    # Call the recipe service to create a new recipe
    success, message = RecipeService.create_recipe(user_email, recipe_data)

    if success:
        return jsonify({'message': message}), 201
    else:
        return jsonify({'message': message}), 400

@recipe_bp.route('/recipes/<recipe_id>', methods=['PUT'])
@jwt_required
def update_recipe(recipe_id):
    user_email = get_jwt_identity()
    updated_data = request.json

    # Call the recipe service to update the recipe
    success, message = RecipeService.update_recipe(user_email, recipe_id, updated_data)

    if success:
        return jsonify({'message': message}), 200
    else:
        return jsonify({'message': message}), 400

@recipe_bp.route('/recipes/<recipe_id>', methods=['DELETE'])
@jwt_required
def delete_recipe(recipe_id):
    user_email = get_jwt_identity()

    # Call the recipe service to delete the recipe
    success, message = RecipeService.delete_recipe(user_email, recipe_id)

    if success:
        return jsonify({'message': message}), 200
    else:
        return jsonify({'message': message}), 400
