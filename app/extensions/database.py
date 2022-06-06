from flask_pymongo import MongoClient

mongo = MongoClient()

def init_app(app):
    return mongo.init_app(app)