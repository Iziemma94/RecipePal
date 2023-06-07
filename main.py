from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import Config
from models import db
from controllers import RecipeController, UserController, AuthenticationController

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
CORS(app)
db.init_app(app)

# API endpoints
api.add_resource(RecipeController, '/recipes', '/recipes/<int:id>')
api.add_resource(UserController, '/users', '/users/<int:id>')
api.add_resource(AuthenticationController, '/login')

if __name__ == '__main__':
    app.run()
