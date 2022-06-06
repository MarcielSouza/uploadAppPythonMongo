from flask import Blueprint,render_template

usuario = Blueprint("usuario",__name__) #passamos como parametro, o nome que daremos 'routes', e passamos o arquivo '__nome__'. esse Blueprint pe referente a esse arquivo em especifico

#O '@' é um decorator que sereve basicamemnte para chamar a nossa rota que dentro da rota fará alguma coisa, nesse caso, a função "def index():"

@usuario.route('/')
def index():
    return "Index"

@usuario.route('/home')
def home():
    return "Home"

@usuario.route("/login")
def login():
    return "Login"

@usuario.route("/Logout")
def logout():
    return "Logout"