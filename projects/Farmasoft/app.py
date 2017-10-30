from flask import Flask, render_template, url_for, redirect, flash, session
from flask_bootstrap import Bootstrap
from forms import LogForm, RegForm, QueryForm
from datetime import datetime
from flask_moment import Moment
from flask_script import Manager
import data_manipulation


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'a random string'

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html',
                                fecha_actual=datetime.utcnow(),
                                username=session.get('username'))
    return render_template('index.html',
                            fecha_actual=datetime.utcnow())

@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LogForm()
    if loginForm.validate_on_submit():
        userData = [loginForm.username.data, loginForm.password.data]
        if data_manipulation.login_data_check(userData):
            session['username'] = loginForm.username.data
            return render_template('login.html',
                                    form=loginForm,
                                    username=session.get('username'))
        else:
            flash('Nombre de usuario o contraseña erroneas')
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
        error = False
        userData = [regForm.username.data, regForm.password.data]
        if data_manipulation.user_duplicate_check(userData[0]):
            error = True
            flash('El usuario ya existe')
        if userData[1] != regForm.repassword.data:
            error = True
            flash('Las contraseñas no coinciden')
        userCreationStatus = data_manipulation.create_user(userData)
        if not error:
            if not userCreationStatus:
                flash('Usuario creado satisfactoriamente! Ahora puede ingresar')
                return redirect('/login')
            else:
                flash('Error al crear el usuario en la base de datos. Codigo {}'.format(userCreationStatus))
    return render_template('register.html', form=regForm)

@app.route('/dataVerification')
def verificacionDatos():
    if 'username' in session:
        fileStatus = data_manipulation.error_check()
        return render_template('dataVerification.html',
                                fileStatus=fileStatus,
                                username=session.get('username'))
    return render_template('dataVerification.html', username=session.get('username'))

@app.route('/lastSales')
def ultimsVentas():
    if 'username' in session:
        salesList = data_manipulation.show_last_sales()
        return render_template('lastSales.html',
                                row1=data_manipulation.HEADERS,
                                dataTable=salesList,
                                username=session.get('username'))
    return render_template('lastSales.html', username=session.get('username'))

@app.route('/mejoresClientes')
def mejoresClientes():
    if 'username' in session:
        clientsList = data_manipulation.show_best_clients()
        fileHeader = ['CLIENTE', 'TOTAL GASTADO']
        return render_template('mejoresClientes.html',
                                row1=fileHeader,
                                dataTable=clientsList,
                                username=session.get('username'))
    return render_template('mejoresClientes.html', username=session.get('username'))

@app.route('/productosMasVendidos')
def productosMasVendidos():
    if 'username' in session:
        productList = data_manipulation.hot_items()
        fileHeader = ['CODIGO', 'PRODUCTO', 'CANTIDAD']
        return render_template('productosMasVendidos.html',
                                row1=fileHeader,
                                dataTable=productList,
                                username=session.get('username'))
    return render_template('productosMasVendidos.html', username=session.get('username'))

@app.route('/productosPorCliente', methods=['GET', 'POST'])
def productosPorCliente():
    if 'username' in session:
        queryForm = QueryForm()
        clientList = data_manipulation.get_client_list()
        # if queryForm.validate_on_submit():
        # No funciona el validate_on_submit, lo salteo con otro if
        if queryForm.autocompleteInput.data in clientList:
            fileHeader = ['CODIGO', 'PRODUCTO', 'CLIENTE', 'CANTIDAD', 'PRECIO']
            productList = data_manipulation.products_by_client(queryForm.autocompleteInput.data)
            return render_template('productosPorCliente.html',
                                    row1=fileHeader,
                                    dataTable=productList,
                                    clientList=clientList,
                                    form=queryForm,
                                    username=session.get('username'))
        flash('Por favor seleccione un cliente de la lista')
    return render_template('productosPorCliente.html',
                            clientList=clientList,
                            form=queryForm,
                            username=session.get('username'))

@app.route('/clientesPorProducto', methods=['GET', 'POST'])
def clientesPorProducto():
    if 'username' in session:
        queryForm = QueryForm()
        productList = data_manipulation.get_product_list()
        # if queryForm.validate_on_submit():
        # No funciona el validate_on_submit, lo salteo con otro if
        if queryForm.autocompleteInput.data in productList:
            fileHeader = ['CODIGO', 'PRODUCTO', 'CLIENTE', 'CANTIDAD', 'PRECIO']
            clientList = data_manipulation.clients_by_product(queryForm.autocompleteInput.data)
            return render_template('clientesPorProducto.html',
                                    row1=fileHeader,
                                    dataTable=clientList,
                                    productList=productList,
                                    form=queryForm,
                                    username=session.get('username'))
        flash('Por favor seleccione un producto de la lista')
    return render_template('clientesPorProducto.html',
                            productList=productList,
                            form=queryForm,
                            username=session.get('username'))

@app.errorhandler(404)
def notFoundError(e):
    return render_template('404.html', username=session.get('username')), 404

@app.errorhandler(500)
def internalError(e):
    return render_template('500.html', username=session.get('username')), 500

@app.errorhandler(FileNotFoundError)
def fileNotFound(e):
    return render_template('fileNotFound.html', username=session.get('username'))

# No es lo ideal, se podria sacar pero intenta
# contemplar cualquier error causado por pandas o csv
@app.errorhandler(Exception)
def fieldError(e):
    return redirect('/dataVerification')


# debug=False o no devuelve codigo de error 500
if __name__ == "__main__":
    app.run(debug=True)