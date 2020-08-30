from flask import render_template

from app.controller.cpf import cpf_bp


@cpf_bp.route('/cpf/')
def validador():
    return render_template('cpf.html')
