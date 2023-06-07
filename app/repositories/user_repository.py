from app.models import User

class UserRepository:
    @staticmethod
    def get_user_by_email(email):
        # Retrieve a user by email from the database
        user = User.query.filter_by(email=email).first()
        return user

    @staticmethod
    def create_user(user_data):
        # Create a new user in the database
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update_user(user, updated_data):
        # Update an existing user in the database
        for key, value in updated_data.items():
            setattr(user, key, value)
        db.session.commit()
