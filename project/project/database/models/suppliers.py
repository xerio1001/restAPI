from project.database.db import db

class Supplier(db.Document):
    supplier = db.StringField(required=True)
    address = db.StringField(required=True)
    phoneNumber = db.StringField(Required=True)
    emailAddress = db.StringField(Required=True)
