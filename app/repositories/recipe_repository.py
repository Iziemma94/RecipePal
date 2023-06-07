from app.models import Recipe

class RecipeRepository:
    @staticmethod
    def get_all_recipes():
        # Retrieve all recipes from the database
        recipes = Recipe.query.all()
        return recipes

    @staticmethod
    def get_recipe_by_id(recipe_id):
        # Retrieve a recipe by its ID from the database
        recipe = Recipe.query.get(recipe_id)
        return recipe

    @staticmethod
    def create_recipe(recipe_data):
        # Create a new recipe in the database
        recipe = Recipe(**recipe_data)
        db.session.add(recipe)
        db.session.commit()

    @staticmethod
    def update_recipe(recipe, updated_data):
        # Update an existing recipe in the database
        for key, value in updated_data.items():
            setattr(recipe, key, value)
        db.session.commit()

    @staticmethod
    def delete_recipe(recipe):
        # Delete a recipe from the database
        db.session.delete(recipe)
        db.session.commit()
