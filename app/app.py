from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

# Create Flask application instance
app = Flask(__name__)

# Load configuration based on environment
app.config.from_object(config['development'])  # Replace 'development' with your desired environment

# Create SQLAlchemy database instance
db = SQLAlchemy(app)

# Import and register blueprints/routes
from app.routes import auth_routes, recipe_routes, user_routes

app.register_blueprint(auth_routes)
app.register_blueprint(recipe_routes)
app.register_blueprint(user_routes)

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables (if they don't exist) before running the app
    app.run(debug=True)
