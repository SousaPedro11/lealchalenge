import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, StopValidation


class CPFForm(FlaskForm):
    string = StringField('Entrada', validators=[DataRequired()])
    submit = SubmitField('Processar')

    def validate_string(self, string):
        if not bool(re.match(r"^(\d{3}.){2}\d{3}-\d{2}$|^\d{11}$", string.data)):
            raise StopValidation('Invalid format!')
