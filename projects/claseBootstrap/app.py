

from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'un string que funcione como llave'

@app.route('/')
def index():
    return render_template('index.html', fecha_actual=datetime.utcnow())

@app.route('/saludar/<usuario>')
def saludar(usuario):
    return render_template('usuario.html', nombre=usuario)

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
    manager.run()
