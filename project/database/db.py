from flask_mongoengine import MongoEngine

db = MongoEngine()

def initiliaze_db(app):
    db.init_app(app)
