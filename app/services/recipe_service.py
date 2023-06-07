from app.repositories.recipe_repository import RecipeRepository

class RecipeService:
    @staticmethod
    def get_all_recipes():
        return RecipeRepository.get_all_recipes()

    @staticmethod
    def get_recipe_by_id(recipe_id):
        return RecipeRepository.get_recipe_by_id(recipe_id)

    @staticmethod
    def create_recipe(recipe_data):
        RecipeRepository.create_recipe(recipe_data)

    @staticmethod
    def update_recipe(recipe_id, updated_data):
        recipe = RecipeRepository.get_recipe_by_id(recipe_id)
        if not recipe:
            return False, "Recipe not found"
        
        RecipeRepository.update_recipe(recipe, updated_data)
        return True, "Recipe updated successfully"

    @staticmethod
    def delete_recipe(recipe_id):
        recipe = RecipeRepository.get_recipe_by_id(recipe_id)
        if not recipe:
            return False, "Recipe not found"
        
        RecipeRepository.delete_recipe(recipe)
        return True, "Recipe deleted successfully"
