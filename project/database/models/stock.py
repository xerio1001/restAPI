from project.database.db import db

class Stock(db.Document):
    name = db.StringField(required=True)
    brand = db.StringField(Required=False)
    price = db.DecimalField(required=True)
    unit = db.Stringfield(required=True)
    amountInStock = db.IntField(required=True)
    amountPerOrder = db.IntField(required=True)
    supplier = db.StringField(required=True)
    barcode = db.StringField(required=False)
    