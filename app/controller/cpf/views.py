from flask import render_template

from app.controller.cpf import cpf_bp
from app.controller.cpf.forms import CPFForm
from .cpf_validator import validar


@cpf_bp.route('/cpf/', methods=['GET', 'POST'])
def validador():
    form = CPFForm()
    retorno = ''
    if form.is_submitted():
        retorno = validar(form.string.data)
    return render_template('cpf.html', form=form, retorno=retorno)
