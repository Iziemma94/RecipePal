import unittest
from unittest.mock import patch, MagicMock
from flask_jwt_extended import create_access_token, create_refresh_token
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository

class UserServiceTest(unittest.TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password': 'password123'
        }

    def test_register_user(self):
        with patch.object(UserRepository, 'get_user_by_email', return_value=None):
            with patch.object(UserRepository, 'create_user') as create_user_mock:
                result, message = UserService.register_user(self.user_data['email'], self.user_data['password'])
                create_user_mock.assert_called_once_with(self.user_data)
                self.assertTrue(result)
                self.assertEqual(message, "User registered successfully")

    def test_register_user_existing_user(self):
        with patch.object(UserRepository, 'get_user_by_email', return_value=MagicMock()):
            result, message = UserService.register_user(self.user_data['email'], self.user_data['password'])
            self.assertFalse(result)
            self.assertEqual(message, "User already exists")

    def test_login_user(self):
        mock_user = MagicMock()
        mock_user.email = self.user_data['email']
        mock_user.password = bcrypt.hashpw(self.user_data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with patch.object(UserRepository, 'get_user_by_email', return_value=mock_user):
            with patch('flask_jwt_extended.create_access_token') as create_access_token_mock:
                with patch('flask_jwt_extended.create_refresh_token') as create_refresh_token_mock:
                    result, access_token, refresh_token = UserService.login_user(self.user_data['email'], self.user_data['password'])
                    create_access_token_mock.assert_called_once_with(identity=self.user_data['email'])
                    create_refresh_token_mock.assert_called_once_with(identity=self.user_data['email'])
                    self.assertTrue(result)
                    self.assertEqual(access_token, create_access_token_mock.return_value)
                    self.assertEqual(refresh_token, create_refresh_token_mock.return_value)

    def test_login_user_invalid_credentials(self):
        with patch.object(UserRepository, 'get_user_by_email', return_value=None):
            result, access_token, refresh_token = UserService.login_user(self.user_data['email'], self.user_data['password'])
            self.assertFalse(result)
            self.assertEqual(access_token, None)
            self.assertEqual(refresh_token, None)

    def test_get_user_profile(self):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.email = self.user_data['email']
        mock_user.created_at = '2023-01-01 00:00:00'
        mock_user.updated_at = '2023-01-01 00:00:00'
        with patch.object(UserRepository, 'get_user_by_email', return_value=mock_user):
            profile = UserService.get_user_profile(self.user_data['email'])
            self.assertEqual(profile, {
                'id': mock_user.id,
                'email': mock_user.email,
                'created_at': mock_user.created_at,
                'updated_at': mock_user.updated_at
            })

    def test_get_user_profile_user_not_found(self):
        with patch.object(UserRepository, 'get_user_by_email', return_value=None):
            profile = UserService.get_user_profile(self.user_data['email'])
            self.assertEqual(profile, None)

    def test_update_user_profile(self):
        mock_user = MagicMock()
        with patch.object(UserRepository, 'get_user_by_email', return_value=mock_user):
            with patch.object(UserRepository, 'update_user') as update_user_mock:
                updated_profile = {'email': 'updated@example.com'}
                result, message = UserService.update_user_profile(self.user_data['email'], updated_profile)
                update_user_mock.assert_called_once_with(mock_user, updated_profile)
                self.assertTrue(result)
                self.assertEqual(message, "User profile updated successfully")

    def test_update_user_profile_user_not_found(self):
        with patch.object(UserRepository, 'get_user_by_email', return_value=None):
            updated_profile = {'email': 'updated@example.com'}
            result, message = UserService.update_user_profile(self.user_data['email'], updated_profile)
            self.assertFalse(result)
            self.assertEqual(message, "User not found")

if __name__ == '__main__':
    unittest.main()
