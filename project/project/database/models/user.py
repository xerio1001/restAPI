from ..db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from project.database.models.stock import Stock

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    function = db.StringField(requiered=True)
    password = db.StringField(required=True, min_length=6) 

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

