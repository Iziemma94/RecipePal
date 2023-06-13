from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import secrets

# Create the Flask application
app = Flask(__name__)

# Generate a random secret key
secret_key = secrets.token_hex(16)

# Set the secret key in the app configuration
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipepal.db'
db = SQLAlchemy(app)
CORS(app)

# Import your routes and controllers here
from controllers.authentication_controller import auth_routes
from controllers.recipe_controller import recipe_routes
from controllers.user_controller import user_routes

# Register the routes
app.register_blueprint(auth_routes)
app.register_blueprint(recipe_routes)
app.register_blueprint(user_routes)

# Run the app
if __name__ == '__main__':
    app.run()
