from flask import render_template

from app.controller.cep import cep_bp


@cep_bp.route('/cep/', methods=['GET', 'POST'])
def cep():
    return render_template('cep.html')
