import unittest
from app import app, db
from app.models.user import User
from app.services.authentication_service import AuthenticationService

class AuthenticationServiceTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()
        self.authentication_service = AuthenticationService()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_user(self):
        user_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password'
        }
        user = self.authentication_service.register(user_data)
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, 'John Doe')

    def test_login_valid_credentials(self):
        user = User(name='John Doe', email='john@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        login_data = {
            'email': 'john@example.com',
            'password': 'password'
        }
        logged_in_user = self.authentication_service.login(login_data)
        self.assertIsInstance(logged_in_user, User)
        self.assertEqual(logged_in_user.email, 'john@example.com')

    def test_login_invalid_credentials(self):
        user = User(name='John Doe', email='john@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        login_data = {
            'email': 'john@example.com',
            'password': 'wrong_password'
        }
        logged_in_user = self.authentication_service.login(login_data)
        self.assertIsNone(logged_in_user)

    def test_logout(self):
        user = User(name='John Doe', email='john@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        token = user.generate_token()
        logged_out_user = self.authentication_service.logout(token)
        self.assertIsInstance(logged_out_user, User)
        self.assertEqual(logged_out_user.email, 'john@example.com')

if __name__ == '__main__':
    unittest.main()
