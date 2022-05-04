from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from project.database.db import initiliaze_db
from flask_restful import Api
from project.resources.routes import initialize_routes
from project.resources.errors import errors

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "t1NP63m4wnBg6nyHYKfmc2TpCOGI4nss"
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.o2oak.mongodb.net/Project?retryWrites=true&w=majority'
}

initiliaze_db(app)
initialize_routes(api)
