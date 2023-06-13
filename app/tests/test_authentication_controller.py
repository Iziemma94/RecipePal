import unittest
import json
from flask import Flask
from app.controllers.authentication_controller import authentication_bp


class AuthenticationControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(authentication_bp)

        # Set up test client
        self.client = self.app.test_client()

    def test_register(self):
        # Create a test user
        test_user = {
            'email': 'test@example.com',
            'password': 'password123'
        }

        # Send a POST request to the register endpoint
        response = self.client.post('/register', json=test_user)
        data = json.loads(response.data.decode())

        # Check the response status code and message
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'User registered successfully')

    def test_login(self):
        # Create a test user
        test_user = {
            'email': 'test@example.com',
            'password': 'password123'
        }

        # Send a POST request to the login endpoint
        response = self.client.post('/login', json=test_user)
        data = json.loads(response.data.decode())

        # Check the response status code and access token
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access_token' in data)

if __name__ == '__main__':
    unittest.main()
