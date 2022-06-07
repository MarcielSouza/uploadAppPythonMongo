import click
from ..extensions.database import mongo
from flask import Blueprint

userComands = Blueprint('user',__name__)

@userComands.cli.command("getUser") 
@click.argument("name")
def get_user(name):
    userCollection = mongo.db.users
    user = [u for u in userCollection.find({"name": name})]
    print(user)