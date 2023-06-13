import unittest
from app import create_app, db
from app.models import Recipe
from app.repositories.recipe_repository import RecipeRepository
from app.services.recipe_service import RecipeService

class RecipeServiceTest(unittest.TestCase):
    def setUp(self):
        # Set up the Flask app for testing
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        # Clean up after each test
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_all_recipes(self):
        # Add sample recipes to the database
        recipe1 = Recipe(title='Recipe 1', description='Description 1')
        recipe2 = Recipe(title='Recipe 2', description='Description 2')
        db.session.add_all([recipe1, recipe2])
        db.session.commit()

        # Get all recipes
        recipes = RecipeService.get_all_recipes()

        # Assert that the correct number of recipes is returned
        self.assertEqual(len(recipes), 2)
        self.assertEqual(recipes[0].title, 'Recipe 1')
        self.assertEqual(recipes[1].title, 'Recipe 2')

    def test_get_recipe_by_id(self):
        # Add a sample recipe to the database
        recipe = Recipe(title='Sample Recipe', description='Sample Description')
        db.session.add(recipe)
        db.session.commit()

        # Get the recipe by ID
        retrieved_recipe = RecipeService.get_recipe_by_id(recipe.id)

        # Assert that the correct recipe is retrieved
        self.assertIsNotNone(retrieved_recipe)
        self.assertEqual(retrieved_recipe.title, 'Sample Recipe')
        self.assertEqual(retrieved_recipe.description, 'Sample Description')

    def test_create_recipe(self):
        # Create a new recipe
        recipe_data = {
            'title': 'New Recipe',
            'description': 'New Description'
        }
        RecipeService.create_recipe(recipe_data)

        # Assert that the recipe is added to the database
        recipes = RecipeRepository.get_all_recipes()
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0].title, 'New Recipe')
        self.assertEqual(recipes[0].description, 'New Description')

    def test_update_recipe(self):
        # Add a sample recipe to the database
        recipe = Recipe(title='Sample Recipe', description='Sample Description')
        db.session.add(recipe)
        db.session.commit()

        # Update the recipe
        updated_data = {
            'title': 'Updated Recipe',
            'description': 'Updated Description'
        }
        success, message = RecipeService.update_recipe(recipe.id, updated_data)

        # Assert that the recipe is updated successfully
        self.assertTrue(success)
        self.assertEqual(message, 'Recipe updated successfully')
        self.assertEqual(recipe.title, 'Updated Recipe')
        self.assertEqual(recipe.description, 'Updated Description')

    def test_update_recipe_not_found(self):
        # Try to update a non-existent recipe
        updated_data = {
            'title': 'Updated Recipe',
            'description': 'Updated Description'
        }
        success, message = RecipeService.update_recipe(1000, updated_data)

        # Assert that the recipe is not found
        self.assertFalse(success)
        self.assertEqual(message, 'Recipe not found')

    def test_delete_recipe(self):
        # Add a sample recipe to the database
        recipe = Recipe(title='Sample Recipe', description='Sample Description')
        db.session.add(recipe)
        db.session.commit()

        # Delete the recipe
        success, message = RecipeService.delete_recipe(recipe.id)

        # Assert that the recipe is deleted successfully
        self.assertTrue(success)
        self.assertEqual(message, 'Recipe deleted successfully')

        # Assert that the recipe is removed from the database
        recipes = RecipeRepository.get_all_recipes()
        self.assertEqual(len(recipes), 0)

    def test_delete_recipe_not_found(self):
        # Try to delete a non-existent recipe
        success, message = RecipeService.delete_recipe(1000)

        # Assert that the recipe is not found
        self.assertFalse(success)
        self.assertEqual(message, 'Recipe not found')

if __name__ == '__main__':
    unittest.main()
