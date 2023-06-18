import unittest
from app.models import User
from app.repositories.user_repository import UserRepository

class UserRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary configurations or dependencies
        pass

    def test_get_user_by_email(self):
        # Create a sample user in the database
        user = User(email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        # Retrieve the user by email using the repository method
        retrieved_user = UserRepository.get_user_by_email('test@example.com')

        # Check if the retrieved user matches the expected user
        self.assertEqual(retrieved_user, user)

    def test_create_user(self):
        # Create a sample user data
        user_data = {
            'email': 'newuser@example.com',
            'password': 'password'
        }

        # Create a new user using the repository method
        UserRepository.create_user(user_data)

        # Retrieve all users from the database
        users = User.query.all()

        # Check if the new user is added to the database
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].email, 'newuser@example.com')

    def test_update_user(self):
        # Create a sample user in the database
        user = User(email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        # Update the user using the repository method
        updated_data = {
            'password': 'newpassword'
        }
        UserRepository.update_user(user, updated_data)

        # Retrieve the updated user from the database
        updated_user = User.query.get(user.id)

        # Check if the user is updated correctly
        self.assertEqual(updated_user.password, 'newpassword')

if __name__ == '__main__':
    unittest.main()
