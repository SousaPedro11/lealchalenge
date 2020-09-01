import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, StopValidation


class CPFForm(FlaskForm):
    string = StringField('Entrada', validators=[DataRequired()])
    submit = SubmitField('Processar')
