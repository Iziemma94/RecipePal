import json
import unittest
from app import app, db
from app.models.user import User

class AuthenticationControllerTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_user(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password123'
        }
        response = self.app.post('/api/register', data=json.dumps(data),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Successfully registered', response.data)

    def test_login_user(self):
        user = User(name='John Doe', email='john@example.com', password='password123')
        db.session.add(user)
        db.session.commit()

        data = {
            'email': 'john@example.com',
            'password': 'password123'
        }
        response = self.app.post('/api/login', data=json.dumps(data),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful', response.data)

    def test_logout_user(self):
        user = User(name='John Doe', email='john@example.com', password='password123')
        db.session.add(user)
        db.session.commit()

        # Log in the user first
        login_data = {
            'email': 'john@example.com',
            'password': 'password123'
        }
        self.app.post('/api/login', data=json.dumps(login_data),
                      headers={'Content-Type': 'application/json'})

        response = self.app.get('/api/logout')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logout successful', response.data)

if __name__ == '__main__':
    unittest.main()
