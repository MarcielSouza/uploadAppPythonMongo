from flask import Flask    #chama a biblioteca
from .routes.usuario import usuario
from .routes.produto import produto
from .extensions import database
 
def create_app():
    app = Flask(__name__)
    app.register_blueprint(usuario)
    app.register_blueprint(produto)
    database.init_app(app)

    return app



