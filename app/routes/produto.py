from flask import Blueprint

produto = Blueprint('produto',__name__)


@produto.route('/list')
def listProdutos():
    return "list"

@produto.route('/insert')
def insertProuto():
    return "insert"

@produto.route('/edit')
def editProduto():
    return 'edit'

@produto.route('/delete')
def deleteProduto():
    return 'delete'