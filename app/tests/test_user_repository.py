import unittest
from app import create_app, db
from app.models import User
from app.repositories.user_repository import UserRepository

class UserRepositoryTest(unittest.TestCase):
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

    def test_get_user_by_email(self):
        # Add a sample user to the database
        user = User(email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        # Call the get_user_by_email method
        retrieved_user = UserRepository.get_user_by_email('test@example.com')

        # Assert that the retrieved user matches the original user
        self.assertEqual(retrieved_user.email, 'test@example.com')
        self.assertEqual(retrieved_user.password, 'password')

    def test_create_user(self):
        # Create a new user
        user_data = {'email': 'new@example.com', 'password': 'password'}
        UserRepository.create_user(user_data)

        # Assert that the user is added to the database
        users = User.query.all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].email, 'new@example.com')
        self.assertEqual(users[0].password, 'password')

    def test_update_user(self):
        # Add a sample user to the database
        user = User(email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        # Update the user
        updated_data = {'email': 'updated@example.com', 'password': 'newpassword'}
        UserRepository.update_user(user, updated_data)

        # Assert that the user is updated in the database
        updated_user = User.query.get(user.id)
        self.assertEqual(updated_user.email, 'updated@example.com')
        self.assertEqual(updated_user.password, 'newpassword')

if __name__ == '__main__':
    unittest.main()
