import json
import unittest
from flask import Flask
from flask_jwt_extended import create_access_token
from app import app
from app.models.recipe import Recipe
from app.controllers.recipe_controller import recipe_bp

class RecipeControllerTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['JWT_SECRET_KEY'] = 'your_secret_key'
        app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
        app.register_blueprint(recipe_bp)
        self.client = app.test_client()

    def test_get_recipes(self):
        # Create a test recipe
        recipe = Recipe(title='Test Recipe', description='This is a test recipe')
        recipe.save()

        # Retrieve the recipes using the API endpoint
        response = self.client.get('/recipes')

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the test recipe
        data = json.loads(response.data)
        self.assertEqual(len(data['recipes']), 1)
        self.assertEqual(data['recipes'][0]['title'], 'Test Recipe')

    def test_create_recipe(self):
        # Create a test access token
        access_token = create_access_token(identity='test@example.com')

        # Create a new recipe using the API endpoint
        response = self.client.post('/recipes', headers={'Authorization': f'Bearer {access_token}'}, json={
            'title': 'New Recipe',
            'description': 'This is a new recipe'
        })

        # Check the response status code
        self.assertEqual(response.status_code, 201)

        # Check if the recipe was created successfully
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Recipe created successfully')

    def test_update_recipe(self):
        # Create a test access token
        access_token = create_access_token(identity='test@example.com')

        # Create a test recipe
        recipe = Recipe(title='Test Recipe', description='This is a test recipe')
        recipe.save()

        # Update the recipe using the API endpoint
        response = self.client.put(f'/recipes/{recipe.id}', headers={'Authorization': f'Bearer {access_token}'}, json={
            'title': 'Updated Recipe',
            'description': 'This is an updated recipe'
        })

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the recipe was updated successfully
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Recipe updated successfully')

    def test_delete_recipe(self):
        # Create a test access token
        access_token = create_access_token(identity='test@example.com')

        # Create a test recipe
        recipe = Recipe(title='Test Recipe', description='This is a test recipe')
        recipe.save()

        # Delete the recipe using the API endpoint
        response = self.client.delete(f'/recipes/{recipe.id}', headers={'Authorization': f'Bearer {access_token}'})

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the recipe was deleted successfully
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Recipe deleted successfully')

if __name__ == '__main__':
    unittest.main()
