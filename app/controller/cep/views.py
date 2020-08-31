from flask import render_template

from app.controller.cep import cep_bp
from app.controller.cep.cep_validator import validar, validar_regex
from app.controller.cep.forms import CEPForm


@cep_bp.route('/cep/', methods=['GET', 'POST'])
def cep():
    retorno = ''
    retorno_regex = ''
    form = CEPForm()
    if form.validate_on_submit():
        string = form.string.data
        retorno = validar(string)
        retorno_regex = validar_regex(string)
    return render_template('cep.html', form=form, retorno=retorno, retorno_regex=retorno_regex)
