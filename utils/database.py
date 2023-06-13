from flask import Flask
from utils.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RecipePal.db'  # Replace with your database URI

db.init_app(app)

# Rest of the app configuration

# Import your routes and controllers here
from controllers.authentication_controller import auth_routes
from controllers.recipe_controller import recipe_routes
from controllers.user_controller import user_routes

# Register the routes
app.register_blueprint(auth_routes)
app.register_blueprint(recipe_routes)
app.register_blueprint(user_routes)

# Run the application
if __name__ == '__main__':
    app.run()
