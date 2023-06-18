import unittest
from unittest.mock import patch
from app.models import User
from app.services.authentication_service import AuthenticationService

class AuthenticationServiceTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary configurations or dependencies
        pass

    @patch('app.repositories.user_repository.UserRepository.get_user_by_email')
    @patch('app.repositories.user_repository.UserRepository.create_user')
    def test_register_user(self, mock_create_user, mock_get_user_by_email):
        # Mock the UserRepository methods
        mock_get_user_by_email.return_value = None

        # Call the register_user method
        success, message = AuthenticationService.register_user('test@example.com', 'password')

        # Check if the UserRepository methods are called correctly
        mock_get_user_by_email.assert_called_once_with('test@example.com')
        mock_create_user.assert_called_once_with({'email': 'test@example.com', 'password': 'hashed_password'})

        # Check the return values
        self.assertTrue(success)
        self.assertEqual(message, 'User registered successfully')

    @patch('app.repositories.user_repository.UserRepository.get_user_by_email')
    def test_register_user_existing_user(self, mock_get_user_by_email):
        # Mock the UserRepository method to return an existing user
        mock_get_user_by_email.return_value = User(email='test@example.com', password='hashed_password')

        # Call the register_user method
        success, message = AuthenticationService.register_user('test@example.com', 'password')

        # Check if the UserRepository method is called correctly
        mock_get_user_by_email.assert_called_once_with('test@example.com')

        # Check the return values
        self.assertFalse(success)
        self.assertEqual(message, 'User already exists')

    @patch('app.repositories.user_repository.UserRepository.get_user_by_email')
    def test_login_user(self, mock_get_user_by_email):
        # Mock the UserRepository method to return a user with matching credentials
        user = User(email='test@example.com', password='hashed_password')
        mock_get_user_by_email.return_value = user

        # Call the login_user method
        success, access_token, refresh_token = AuthenticationService.login_user('test@example.com', 'password')

        # Check if the UserRepository method is called correctly
        mock_get_user_by_email.assert_called_once_with('test@example.com')

        # Check the return values
        self.assertTrue(success)
        self.assertIsNotNone(access_token)
        self.assertIsNotNone(refresh_token)

    @patch('app.repositories.user_repository.UserRepository.get_user_by_email')
    def test_login_user_invalid_credentials(self, mock_get_user_by_email):
        # Mock the UserRepository method to return None (no user with the given email)
        mock_get_user_by_email.return_value = None

        # Call the login_user method
        success, access_token, refresh_token = AuthenticationService.login_user('test@example.com', 'password')

        # Check if the UserRepository method is called correctly
        mock_get_user_by_email.assert_called_once_with('test@example.com')

        # Check the return values
        self.assertFalse(success)
        self.assertIsNone(access_token)
        self.assertIsNone(refresh_token)

if __name__ == '__main__':
    unittest.main()
