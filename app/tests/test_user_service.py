import unittest
from app import app, db
from app.models.user import User
from app.services.user_service import UserService

class UserServiceTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()
        self.user_service = UserService()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_user(self):
        user = User(name='John Doe', email='john@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        retrieved_user = self.user_service.get_user(user.id)
        self.assertIsInstance(retrieved_user, User)
        self.assertEqual(retrieved_user.email, 'john@example.com')

    def test_update_user(self):
        user = User(name='John Doe', email='john@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        user_data = {
            'name': 'John Smith',
            'email': 'john.smith@example.com'
        }
        updated_user = self.user_service.update_user(user.id, user_data)
        self.assertIsInstance(updated_user, User)
        self.assertEqual(updated_user.name, 'John Smith')

    def test_delete_user(self):
        user = User(name='John Doe', email='john@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        deleted_user = self.user_service.delete_user(user.id)
        self.assertIsInstance(deleted_user, User)
        self.assertEqual(deleted_user.email, 'john@example.com')

if __name__ == '__main__':
    unittest.main()
