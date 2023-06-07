import bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token

from app.repositories.user_repository import UserRepository

class AuthenticationService:
    @staticmethod
    def register_user(email, password):
        # Check if the user already exists
        existing_user = UserRepository.get_user_by_email(email)
        if existing_user:
            return False, "User already exists"

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create a new user
        user_data = {
            'email': email,
            'password': hashed_password
        }
        UserRepository.create_user(user_data)

        return True, "User registered successfully"

    @staticmethod
    def login_user(email, password):
        # Retrieve the user by email
        user = UserRepository.get_user_by_email(email)
        if not user:
            return False, "Invalid credentials"

        # Check the password
        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return False, "Invalid credentials"

        # Generate access token and refresh token
        access_token = create_access_token(identity=user.email)
        refresh_token = create_refresh_token(identity=user.email)

        return True, access_token, refresh_token
