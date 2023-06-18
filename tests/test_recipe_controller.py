import unittest
import json
from flask import Flask
from flask_jwt_extended import create_access_token, JWTManager
from app.controllers.recipe_controller import recipe_bp


class RecipeControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['JWT_SECRET_KEY'] = 'your_secret_key'
        self.jwt = JWTManager(self.app)

        self.app.register_blueprint(recipe_bp)

        # Set up test client
        self.client = self.app.test_client()

    def test_create_recipe(self):
        # Create a test recipe
        test_recipe = {
            'name': 'Test Recipe',
            'instructions': 'Test instructions',
            'ingredients': ['Ingredient 1', 'Ingredient 2']
        }

        # Generate an access token for a user
        access_token = create_access_token(identity='test@example.com')

        # Send a POST request to the create_recipe endpoint with the access token
        response = self.client.post('/recipes', json=test_recipe, headers={'Authorization': 'Bearer {}'.format(access_token)})
        data = json.loads(response.data.decode())

        # Check the response status code and message
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Recipe created successfully')

    def test_update_recipe(self):
        # Create a test recipe
        test_recipe = {
            'name': 'Test Recipe',
            'instructions': 'Test instructions',
            'ingredients': ['Ingredient 1', 'Ingredient 2']
        }

        # Generate an access token for a user
        access_token = create_access_token(identity='test@example.com')

        # Send a POST request to the create_recipe endpoint with the access token
        response = self.client.post('/recipes', json=test_recipe, headers={'Authorization': 'Bearer {}'.format(access_token)})
        data = json.loads(response.data.decode())

        # Get the created recipe ID
        recipe_id = data['recipe']['id']

        # Update the test recipe
        updated_recipe = {
            'name': 'Updated Recipe',
            'instructions': 'Updated instructions',
            'ingredients': ['Updated Ingredient 1', 'Updated Ingredient 2']
        }

        # Send a PUT request to the update_recipe endpoint with the access token
        response = self.client.put('/recipes/{}'.format(recipe_id), json=updated_recipe, headers={'Authorization': 'Bearer {}'.format(access_token)})
        data = json.loads(response.data.decode())

        # Check the response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Recipe updated successfully')

    def test_delete_recipe(self):
        # Create a test recipe
        test_recipe = {
            'name': 'Test Recipe',
            'instructions': 'Test instructions',
            'ingredients': ['Ingredient 1', 'Ingredient 2']
        }

        # Generate an access token for a user
        access_token = create_access_token(identity='test@example.com')

        # Send a POST request to the create_recipe endpoint with the access token
        response = self.client.post('/recipes', json=test_recipe, headers={'Authorization': 'Bearer {}'.format(access_token)})
        data = json.loads(response.data.decode())

        # Get the created recipe ID
        recipe_id = data['recipe']['id']

        # Send a DELETE request to the delete_recipe endpoint with the access token
        response = self.client.delete('/recipes/{}'.format(recipe_id), headers={'Authorization': 'Bearer {}'.format(access_token)})
        data = json.loads(response.data.decode())

        # Check the response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Recipe deleted successfully')

if __name__ == '__main__':
    unittest.main()
