from flask import Flask    #chama a biblioteca
from .extensions import database
from .routes.usuario import usuario
from .routes.produto import produto
from .commands.userCommands import userComands

def create_app():
    app = Flask(__name__)    
    app.config["MONGO_URI"] = "mongodb+srv://marque:<password>@hands-on.fnmzd.mongodb.net/handsOn?retryWrites=true&w=majority"
    app.register_blueprint(usuario)
    app.register_blueprint(produto)
    app.register_blueprint(userComands)
    database.init_app(app)

    return app



