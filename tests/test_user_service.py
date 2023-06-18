import unittest
from unittest.mock import patch
from app.models import User
from app.services.user_service import UserService

class UserServiceTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary configurations or dependencies
        pass

    @patch('app.repositories.user_repository.UserRepository.get_user_by_email')
    def test_register_user(self, mock_get_user_by_email):
        # Mock the UserRepository method
        mock_get_user_by_email.return_value = None

        # Call the register_user method
        email = 'test@example.com'
        password = 'password123'
        success, message = UserService.register_user(email, password)

        # Check if the UserRepository method is called correctly
        mock_get_user_by_email.assert_called_once_with(email)

        # Check the return values
        self.assertTrue(success)
        self.assertEqual(message, 'User registered successfully')

    @patch('app.repositories.user_repository.UserRepository.get_user_by_email')
    def test_register_user_existing_user(self, mock_get_user_by_email):
        # Mock the UserRepository method
        mock_get_user_by_email.return_value = User(id=1, email='test@example.com', password='hashed_password')

        # Call the register_user method
        email = 'test@example.com'
        password = 'password123'
        success, message = UserService.register_user(email, password)

        # Check if the UserRepository method is called correctly
        mock_get_user_by_email.assert_called_once_with(email)

        # Check the return values
        self.assertFalse(success)
        self.assertEqual(message, 'User already exists')

    @patch('app.repositories.user_repository.UserRepository.get_user_by_email')
    def test_login_user(self, mock_get_user_by_email):
        # Mock the UserRepository method
        mock_get_user_by_email.return_value = User(id=1, email='test@example.com', password='$2b$12$NzVX')

        # Call the login_user method
        email = 'test@example.com'
        password = 'password123'
        success, access_token, refresh_token = UserService.login_user(email, password)

        # Check if the UserRepository method is called correctly
        mock_get_user_by_email.assert_called_once_with(email)

        # Check the return values
        self.assertTrue(success)
        self.assertIsNotNone(access_token)
        self.assertIsNotNone(refresh_token)

    @patch('app.repositories.user_repository.UserRepository.get_user_by_email')
    def test_login_user_invalid_credentials(self, mock_get_user_by_email):
        # Mock the UserRepository method
        mock_get_user_by_email.return_value = None

        # Call the login_user method
        email = 'test@example.com'
        password = 'password123'
        success, message = UserService.login_user(email, password)

        # Check if the UserRepository method is called correctly
        mock_get_user_by_email.assert_called_once_with(email)

        # Check the return values
        self.assertFalse(success)
        self.assertEqual(message, 'Invalid credentials')

    @patch('app.repositories.user_repository.UserRepository.get_user_by_email')
    def test_get_user_profile(self, mock_get_user_by_email):
        # Mock the UserRepository method
        mock_get_user_by_email.return_value = User(id=1, email='test@example.com')

        # Call the get_user_profile method
        email = 'test@example.com'
        user_profile = UserService.get_user_profile(email)

        # Check if the UserRepository method is called correctly
        mock_get_user_by_email.assert_called_once_with(email)

        # Check the return value
        self.assertEqual(user_profile['email'], 'test@example.com')

    @patch('app.repositories.user_repository.UserRepository.get_user_by_email')
    @patch('app.repositories.user_repository.UserRepository.update_user')
    def test_update_user_profile(self, mock_update_user, mock_get_user_by_email):
        # Mock the UserRepository methods
        mock_get_user_by_email.return_value = User(id=1, email='test@example.com')
        mock_update_user.return_value = None

        # Call the update_user_profile method
        email = 'test@example.com'
        updated_profile = {'email': 'newemail@example.com'}
        success, message = UserService.update_user_profile(email, updated_profile)

        # Check if the UserRepository methods are called correctly
        mock_get_user_by_email.assert_called_once_with(email)
        mock_update_user.assert_called_once()

        # Check the return values
        self.assertTrue(success)
        self.assertEqual(message, 'User profile updated successfully')

if __name__ == '__main__':
    unittest.main()
