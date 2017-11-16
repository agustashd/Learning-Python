from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class LogForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    repassword = PasswordField('Enter password again:', validators=[DataRequired()])
    submit = SubmitField('Register')

class EditForm(FlaskForm):
    password = PasswordField('Password:', validators=[DataRequired()])
    repassword = PasswordField('Enter password again:', validators=[DataRequired()])
    submit = SubmitField('Save')

class QueryForm(FlaskForm):
    autocompleteInput = StringField('autocompleteInput', validators=[DataRequired()])