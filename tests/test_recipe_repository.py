import unittest
from app.models import Recipe
from app.repositories.recipe_repository import RecipeRepository

class RecipeRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary configurations or dependencies
        pass

    def test_get_all_recipes(self):
        # Create sample recipes in the database
        recipe1 = Recipe(name='Recipe 1', description='Description 1')
        recipe2 = Recipe(name='Recipe 2', description='Description 2')
        # Add the recipes to the session
        db.session.add(recipe1)
        db.session.add(recipe2)
        db.session.commit()

        # Retrieve all recipes using the repository method
        recipes = RecipeRepository.get_all_recipes()

        # Check if the returned recipes match the expected number
        self.assertEqual(len(recipes), 2)

    def test_get_recipe_by_id(self):
        # Create a sample recipe in the database
        recipe = Recipe(name='Recipe', description='Description')
        db.session.add(recipe)
        db.session.commit()

        # Retrieve the recipe by its ID using the repository method
        retrieved_recipe = RecipeRepository.get_recipe_by_id(recipe.id)

        # Check if the retrieved recipe matches the expected recipe
        self.assertEqual(retrieved_recipe, recipe)

    def test_create_recipe(self):
        # Create a sample recipe data
        recipe_data = {
            'name': 'New Recipe',
            'description': 'New Description'
        }

        # Create a new recipe using the repository method
        RecipeRepository.create_recipe(recipe_data)

        # Retrieve all recipes from the database
        recipes = Recipe.query.all()

        # Check if the new recipe is added to the database
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0].name, 'New Recipe')
        self.assertEqual(recipes[0].description, 'New Description')

    def test_update_recipe(self):
        # Create a sample recipe in the database
        recipe = Recipe(name='Recipe', description='Description')
        db.session.add(recipe)
        db.session.commit()

        # Update the recipe using the repository method
        updated_data = {
            'name': 'Updated Recipe',
            'description': 'Updated Description'
        }
        RecipeRepository.update_recipe(recipe, updated_data)

        # Retrieve the updated recipe from the database
        updated_recipe = Recipe.query.get(recipe.id)

        # Check if the recipe is updated correctly
        self.assertEqual(updated_recipe.name, 'Updated Recipe')
        self.assertEqual(updated_recipe.description, 'Updated Description')

    def test_delete_recipe(self):
        # Create a sample recipe in the database
        recipe = Recipe(name='Recipe', description='Description')
        db.session.add(recipe)
        db.session.commit()

        # Delete the recipe using the repository method
        RecipeRepository.delete_recipe(recipe)

        # Check if the recipe is deleted from the database
        deleted_recipe = Recipe.query.get(recipe.id)
        self.assertIsNone(deleted_recipe)

if __name__ == '__main__':
    unittest.main()
