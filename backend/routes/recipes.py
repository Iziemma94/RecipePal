from flask import Blueprint, request, jsonify, g
from app import db
from models.recipe import Recipe
from models.user import User

recipes_bp = Blueprint('recipes', __name__)

@recipes_bp.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    recipe_list = []

    for recipe in recipes:
        recipe_list.append({
            'id': recipe.id,
            'name': recipe.name,
            'ingredients': recipe.ingredients,
            'directions': recipe.directions,
            'category': recipe.category,
            'user_id': recipe.user_id
        })

    return jsonify(recipe_list), 200

@recipes_bp.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    name = data.get('name')
    ingredients = data.get('ingredients')
    directions = data.get('directions')
    category = data.get('category')

    if not name or not ingredients or not directions or not category:
        return jsonify({'message': 'Please provide all required fields'}), 400

    new_recipe = Recipe(name=name, ingredients=ingredients, directions=directions, category=category, user_id=g.user.id)

    db.session.add(new_recipe)
    db.session.commit()

    return jsonify({'message': 'Recipe created successfully'}), 201

@recipes_bp.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if not recipe:
        return jsonify({'message': 'Recipe not found'}), 404

    data = request.get_json()
    name = data.get('name')
    ingredients = data.get('ingredients')
    directions = data.get('directions')
    category = data.get('category')

    if not name or not ingredients or not directions or not category:
        return jsonify({'message': 'Please provide all required fields'}), 400

    recipe.name = name
    recipe.ingredients = ingredients
    recipe.directions = directions
    recipe.category = category

    db.session.commit()

    return jsonify({'message': 'Recipe updated successfully'}), 200

@recipes_bp.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if not recipe:
        return jsonify({'message': 'Recipe not found'}), 404

    db.session.delete(recipe)
    db.session.commit()

    return jsonify({'message': 'Recipe deleted successfully'}), 200
