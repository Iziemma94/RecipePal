import unittest
from app import create_app, db
from app.models import Recipe
from app.repositories.recipe_repository import RecipeRepository

class RecipeRepositoryTest(unittest.TestCase):
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

        # Call the get_all_recipes method
        recipes = RecipeRepository.get_all_recipes()

        # Assert that the correct number of recipes is retrieved
        self.assertEqual(len(recipes), 2)

    def test_get_recipe_by_id(self):
        # Add a sample recipe to the database
        recipe = Recipe(title='Recipe', description='Description')
        db.session.add(recipe)
        db.session.commit()

        # Call the get_recipe_by_id method
        retrieved_recipe = RecipeRepository.get_recipe_by_id(recipe.id)

        # Assert that the retrieved recipe matches the original recipe
        self.assertEqual(retrieved_recipe.title, 'Recipe')
        self.assertEqual(retrieved_recipe.description, 'Description')

    def test_create_recipe(self):
        # Create a new recipe
        recipe_data = {'title': 'New Recipe', 'description': 'New Description'}
        RecipeRepository.create_recipe(recipe_data)

        # Assert that the recipe is added to the database
        recipes = Recipe.query.all()
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0].title, 'New Recipe')
        self.assertEqual(recipes[0].description, 'New Description')

    def test_update_recipe(self):
        # Add a sample recipe to the database
        recipe = Recipe(title='Recipe', description='Description')
        db.session.add(recipe)
        db.session.commit()

        # Update the recipe
        updated_data = {'title': 'Updated Recipe', 'description': 'Updated Description'}
        RecipeRepository.update_recipe(recipe, updated_data)

        # Assert that the recipe is updated in the database
        updated_recipe = Recipe.query.get(recipe.id)
        self.assertEqual(updated_recipe.title, 'Updated Recipe')
        self.assertEqual(updated_recipe.description, 'Updated Description')

    def test_delete_recipe(self):
        # Add a sample recipe to the database
        recipe = Recipe(title='Recipe', description='Description')
        db.session.add(recipe)
        db.session.commit()

        # Delete the recipe
        RecipeRepository.delete_recipe(recipe)

        # Assert that the recipe is deleted from the database
        deleted_recipe = Recipe.query.get(recipe.id)
        self.assertIsNone(deleted_recipe)

if __name__ == '__main__':
    unittest.main()
