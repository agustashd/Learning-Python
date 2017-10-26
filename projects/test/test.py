from flask import Flask, render_template, redirect, flash, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from datetime import datetime
from flask_moment import Moment
from flask_script import Manager
import csv

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'a random string'

class LogForm(FlaskForm):
    name = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegForm(FlaskForm):
    name = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    repassword = PasswordField('Enter password again:', validators=[DataRequired()])
    submit = SubmitField('Register')

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', fecha_actual=datetime.utcnow(), username=session.get('username'))
    return render_template('index.html', fecha_actual=datetime.utcnow())

@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LogForm()
    if loginForm.validate_on_submit():
        user_password = [loginForm.name.data, loginForm.password.data]
        with open('users.csv', newline='') as csvFile:
            filereader = csv.reader(csvFile)
            found = False
            for row in filereader:
                if user_password == row:
                    found = True
                    session['username'] = loginForm.name.data
                    return render_template('login.html',
                                            form=loginForm,
                                            username=session.get('username'))
            if found is False:
                flash('Wrong username or password')
                return redirect('/login')
    return render_template('login.html',
                            form=loginForm,
                            username=session.get('username'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    regForm = RegForm()
    if regForm.validate_on_submit():
        duplicate = False
        with open('users.csv', newline='') as csvFile:
            filereader = csv.reader(csvFile)
            for row in filereader:
                if regForm.name.data == row[0]:
                    duplicate = True
        if duplicate:
            flash('Username already exists')
        elif regForm.password.data != regForm.repassword.data:
            flash('Password does not match')
        else:
            with open('users.csv', 'a', newline='') as csvFile:
                filewriter = csv.writer(csvFile)
                filewriter.writerow([regForm.name.data, regForm.password.data])
            return redirect('/login')
    return render_template('register.html', form=regForm)

@app.route('/data', methods=['GET', 'POST'])
def data():
    if 'username' in session:
        with open('data.csv', newline='') as csvFile:
            dataTable = csv.reader(csvFile)
            row1 = next(dataTable)
            return render_template('data.html',
                                    row1=row1,
                                    data_table=data_table,
                                    username=session.get('username'))
    else:
        return render_template('data.html', username=session.get('username'))

if __name__ == "__main__":
    app.run(debug=True)