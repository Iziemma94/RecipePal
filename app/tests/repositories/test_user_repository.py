import unittest
from app import app, db
from app.models.user import User
from app.repositories.user_repository import UserRepository

class UserRepositoryTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()
        self.user_repository = UserRepository()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        user_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password'
        }
        user = self.user_repository.create(user_data)
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, 'John Doe')

    def test_get_user_by_email(self):
        user = User(name='John Doe', email='john@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        retrieved_user = self.user_repository.get_by_email('john@example.com')
        self.assertIsInstance(retrieved_user, User)
        self.assertEqual(retrieved_user.name, 'John Doe')

    def test_update_user(self):
        user = User(name='John Doe', email='john@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        user_data = {
            'name': 'John Smith',
            'email': 'john@example.com',
            'password': 'new_password'
        }
        updated_user = self.user_repository.update(user.id, user_data)
        self.assertIsInstance(updated_user, User)
        self.assertEqual(updated_user.name, 'John Smith')
        self.assertNotEqual(updated_user.password, 'password')

    def test_delete_user(self):
        user = User(name='John Doe', email='john@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        deleted_user = self.user_repository.delete(user.id)
        self.assertIsInstance(deleted_user, User)
        self.assertEqual(deleted_user.name, 'John Doe')

if __name__ == '__main__':
    unittest.main()
