from app.controller.endereco import endereco_bp


@endereco_bp.route('/enderecos/', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def enderecos():
    pass
