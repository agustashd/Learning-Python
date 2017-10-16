from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired

class MiFormulario(FlaskForm):
    name = StringField('Ingrese cuenta bancaria', validators=[DataRequired()])
    submit = SubmitField('Ìngresar')

