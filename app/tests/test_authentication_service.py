import unittest
from app import create_app, db
from app.models import User
from app.repositories.user_repository import UserRepository
from app.services.authentication_service import AuthenticationService

class AuthenticationServiceTest(unittest.TestCase):
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

    def test_register_user(self):
        # Register a new user
        email = 'test@example.com'
        password = 'password'
        success, message = AuthenticationService.register_user(email, password)

        # Assert that the user is registered successfully
        self.assertTrue(success)
        self.assertEqual(message, 'User registered successfully')

        # Assert that the user is added to the database
        user = UserRepository.get_user_by_email(email)
        self.assertIsNotNone(user)
        self.assertEqual(user.email, email)

    def test_login_user(self):
        # Add a sample user to the database
        email = 'test@example.com'
        password = 'password'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = User(email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        # Login the user
        success, access_token, refresh_token = AuthenticationService.login_user(email, password)

        # Assert that the login is successful and tokens are generated
        self.assertTrue(success)
        self.assertIsNotNone(access_token)
        self.assertIsNotNone(refresh_token)

    def test_login_user_invalid_credentials(self):
        # Try to login with invalid credentials
        email = 'test@example.com'
        password = 'wrongpassword'
        success, access_token, refresh_token = AuthenticationService.login_user(email, password)

        # Assert that the login fails with invalid credentials
        self.assertFalse(success)
        self.assertIsNone(access_token)
        self.assertIsNone(refresh_token)

if __name__ == '__main__':
    unittest.main()
