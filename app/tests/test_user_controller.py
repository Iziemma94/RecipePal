import json
import unittest
from flask import Flask
from flask_jwt_extended import create_access_token
from app import app
from app.models.user import User
from app.controllers.user_controller import user_bp

class UserControllerTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['JWT_SECRET_KEY'] = 'your_secret_key'
        app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
        app.register_blueprint(user_bp)
        self.client = app.test_client()

    def test_get_user_profile(self):
        # Create a test user
        user = User(email='test@example.com', password='password')
        user.save()

        # Create a test access token
        access_token = create_access_token(identity=user.email)

        # Retrieve the user profile using the API endpoint
        response = self.client.get('/users/profile', headers={'Authorization': f'Bearer {access_token}'})

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the user profile
        data = json.loads(response.data)
        self.assertEqual(data['email'], 'test@example.com')

    def test_update_user_profile(self):
        # Create a test user
        user = User(email='test@example.com', password='password')
        user.save()

        # Create a test access token
        access_token = create_access_token(identity=user.email)

        # Update the user profile using the API endpoint
        response = self.client.put('/users/profile', headers={'Authorization': f'Bearer {access_token}'}, json={
            'name': 'John Doe',
            'age': 30
        })

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the user profile was updated successfully
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'User profile updated successfully')

    def test_get_user_recipes(self):
        # Create a test user
        user = User(email='test@example.com', password='password')
        user.save()

        # Create a test access token
        access_token = create_access_token(identity=user.email)

        # Retrieve the user's recipes using the API endpoint
        response = self.client.get('/users/recipes', headers={'Authorization': f'Bearer {access_token}'})

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the user's recipes
        data = json.loads(response.data)
        self.assertEqual(len(data['recipes']), 0)

    def test_get_user_favorites(self):
        # Create a test user
        user = User(email='test@example.com', password='password')
        user.save()

        # Create a test access token
        access_token = create_access_token(identity=user.email)

        # Retrieve the user's favorite recipes using the API endpoint
        response = self.client.get('/users/favorites', headers={'Authorization': f'Bearer {access_token}'})

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the user's favorite recipes
        data = json.loads(response.data)
        self.assertEqual(len(data['favorites']), 0)

if __name__ == '__main__':
    unittest.main()
