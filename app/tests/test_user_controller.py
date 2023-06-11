import json
import unittest
from app import app, db
from app.models.user import User

class UserControllerTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_user_profile(self):
        user = User(name='John Doe', email='john@example.com')
        db.session.add(user)
        db.session.commit()

        response = self.app.get('/api/user/profile')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Doe', response.data)

    def test_update_user_profile(self):
        user = User(name='John Doe', email='john@example.com')
        db.session.add(user)
        db.session.commit()

        data = {
            'name': 'John Smith',
            'email': 'john@example.com'
        }
        response = self.app.put('/api/user/profile', data=json.dumps(data),
                                headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Profile updated successfully', response.data)

    def test_delete_user(self):
        user = User(name='John Doe', email='john@example.com')
        db.session.add(user)
        db.session.commit()

        response = self.app.delete('/api/user')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User deleted successfully', response.data)

if __name__ == '__main__':
    unittest.main()
