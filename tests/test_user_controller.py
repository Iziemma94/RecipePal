import unittest
import json
from flask import Flask
from flask_jwt_extended import create_access_token
from app.controllers.user_controller import user_bp


class UserControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['JWT_SECRET_KEY'] = 'test_secret_key'
        self.app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False

        self.app.register_blueprint(user_bp)

        # Set up test client
        self.client = self.app.test_client()

    def get_access_token(self):
        # Generate a test access token
        with self.app.app_context():
            access_token = create_access_token(identity='test@example.com')
            return access_token

    def test_get_user_profile(self):
        # Send a GET request to the user profile endpoint
        access_token = self.get_access_token()
        headers = {'Authorization': f'Bearer {access_token}'}
        response = self.client.get('/users/profile', headers=headers)
        data = json.loads(response.data.decode())

        # Check the response status code and data
        self.assertEqual(response.status_code, 200)
        self.assertTrue('user_profile' in data)

    def test_update_user_profile(self):
        # Update the test user profile
        updated_profile = {
            'name': 'John Doe',
            'location': 'New York'
        }

        # Send a PUT request to the update user profile endpoint
        access_token = self.get_access_token()
        headers = {'Authorization': f'Bearer {access_token}'}
        response = self.client.put('/users/profile', json=updated_profile, headers=headers)
        data = json.loads(response.data.decode())

        # Check the response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'User profile updated successfully')

    def test_get_user_recipes(self):
        # Send a GET request to the user recipes endpoint
        access_token = self.get_access_token()
        headers = {'Authorization': f'Bearer {access_token}'}
        response = self.client.get('/users/recipes', headers=headers)
        data = json.loads(response.data.decode())

        # Check the response status code and data
        self.assertEqual(response.status_code, 200)
        self.assertTrue('recipes' in data)

    def test_get_user_favorites(self):
        # Send a GET request to the user favorites endpoint
        access_token = self.get_access_token()
        headers = {'Authorization': f'Bearer {access_token}'}
        response = self.client.get('/users/favorites', headers=headers)
        data = json.loads(response.data.decode())

        # Check the response status code and data
        self.assertEqual(response.status_code, 200)
        self.assertTrue('favorites' in data)

if __name__ == '__main__':
    unittest.main()
