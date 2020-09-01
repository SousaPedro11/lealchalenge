from flask import render_template

from app.controller.cpf import cpf_bp
from app.controller.cpf.forms import CPFForm
from .cpf_validator import validar


@cpf_bp.route('/cpf/', methods=['GET', 'POST'])
def validador():
    form = CPFForm()
    if form.validate_on_submit():
        retorno = form.string.data
        retorno = validar(retorno)
        return render_template('cpf_retorno.html', form=form, retorno=retorno)

    return render_template('cpf.html', form=form)
