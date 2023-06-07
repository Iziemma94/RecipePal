from flask import Flask
from utils.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipepal.db'  # Replace with your database URI

db.init_app(app)

# Rest of the app configuration, routes, and run statement...
