# -*- coding: utf-8 -*-
'''
    data_manipulation Module
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Modulo para manipular los archivos de la app de farmasoft

'''
import pandas as pd
import csv
USERS_DATA = 'users.csv'
STORE_DATA = 'data.csv'
    
# Guardo los nombres de las columnas en el orden que quiero
# mostrarlas en las vistas de la app
HEADERS = ['CODIGO', 'PRODUCTO', 'CLIENTE', 'CANTIDAD', 'PRECIO']

# Antes de importar pandas para facilitar la parte de las consultas
# cree esta funcion usando solo csv, se podria haber usado
# pandas para todo
def error_check():
    '''
    Chequea errores en el archivo de datos de la farmacia sin saber
    el orden de las columnas
    Returns: lista con los errores
    '''
    with open(STORE_DATA, newline='') as csvFile:
        n = 0
        errorList = []
        filereader = csv.reader(csvFile)
        fileHeader = next(filereader)
        codigo = fileHeader.index(HEADERS[0])
        producto = fileHeader.index(HEADERS[1])
        cliente = fileHeader.index(HEADERS[2])
        cantidad = fileHeader.index(HEADERS[3])
        precio = fileHeader.index(HEADERS[4])
        for row in filereader:
            n += 1
            if len(row) != 5:
                errorList.append('La linea {} de la base de datos tiene un numero invalido de campos.'.format(n))
            if row[codigo] == '':
                errorList.append('El campo CODIGO de la linea {} de la base de datos esta vacio.'.format(n))
            try:
                int(float(row[cantidad]))
            except ValueError:
                errorList.append('El campo CANTIDAD de la linea {} de la base de datos no es un numero entero.'.format(n))
            try:
                float(row[precio])
            except ValueError:
                errorList.append('El campo PRECIO de la linea {} de la base de datos no es un valor decimal.'.format(n))
    return errorList

def login_data_check(userData):
    '''
    Verifica que username y password esten en el csv
    userData: ['username', 'password']
    Returns: booleano indicando si se encontro o no el usuario
    '''
    found = False
    with open(USERS_DATA, newline='') as csvFile:
        filereader = csv.reader(csvFile)
        for row in filereader:
            if userData == row:
                found = True
    return found

def user_duplicate_check(usernameFormData):
    '''
    Verifica si el nombre de usuario ya existe
    usernameFormData:username devuelto por el formulario
    Returns: booleano indicando si se encontro o no un duplicado
    '''
    duplicate = False
    with open(USERS_DATA, newline='') as csvFile:
        filereader = csv.reader(csvFile)
        for row in filereader:
            if usernameFormData == row[0]:
                duplicate = True
    return duplicate

def create_user(userData):
    '''
    Intenta escribir en el csv una fila con el username y password
    userData: ['username', 'password']
    Returns: 0 si creo el usuario o message como mensaje de error
    '''
    with open('users.csv', 'a', newline='') as csvFile:
        filewriter = csv.writer(csvFile)
        try:
            filewriter.writerow(userData)
            return 0
        except csv.Error as message:
            return message     

def show_last_sales():
    '''
    Obtiene las ventas mas nuevas
    Returns: objeto iterable con los resultados
    '''
    df = pd.read_csv(STORE_DATA)
    salesList = df.tail(5).iloc[::-1]
    salesList.to_csv('tabla.csv', index=False)
    salesList = salesList.as_matrix()
    return salesList

def get_client_list():
    '''
    Returns: una lista de los clientes
    '''
    df = pd.read_csv(STORE_DATA)
    clientList = df['CLIENTE'].drop_duplicates().tolist()
    return clientList

def products_by_client(clientName):
    '''
    Muestra los productos que compro un cliente
    clientName: string con el nombre completo del cliente
    Returns: objeto iterable con los resultados
    '''
    df = pd.read_csv(STORE_DATA)
    productList = df[df.CLIENTE == clientName]
    productList = productList.groupby(by=['CODIGO', 'CLIENTE', 'PRODUCTO'], as_index=False).sum().iloc[::-1]
    productList.to_csv('tabla.csv', columns=['CODIGO', 'PRODUCTO', 'CLIENTE', 'CANTIDAD', 'PRECIO'], index=False)
    productList = productList.as_matrix(columns=['CODIGO', 'PRODUCTO', 'CLIENTE', 'CANTIDAD', 'PRECIO'])
    return productList

def get_product_list():
    '''
    Returns: una lista de los productos
    '''
    df = pd.read_csv(STORE_DATA)
    productList = df['PRODUCTO'].drop_duplicates().tolist()
    return productList

def clients_by_product(productName):
    '''
    Muestra los productos que compro un cliente
    clientName: string con el nombre completo del cliente
    Returns: objeto iterable con los resultados
    '''
    df = pd.read_csv(STORE_DATA)
    clientList = df[df.PRODUCTO == productName]
    clientList = clientList.groupby(by=['CODIGO', 'CLIENTE', 'PRODUCTO'], as_index=False).sum().iloc[::-1]
    clientList.to_csv('tabla.csv',columns=['CODIGO', 'PRODUCTO', 'CLIENTE', 'CANTIDAD', 'PRECIO'], index=False)
    clientList = clientList.as_matrix(columns=['CODIGO', 'PRODUCTO', 'CLIENTE', 'CANTIDAD', 'PRECIO'])
    return clientList

def hot_items():
    '''
    Muestra los productos mas vendidos
    Returns: objeto iterable con los resultados
    '''
    df = pd.read_csv(STORE_DATA)
    productsList = df.groupby(by=['PRODUCTO'], as_index=False).sum()
    productsList = productsList.sort_values(by=['CANTIDAD'])
    productsList = productsList.tail(5).iloc[::-1]
    productsList.to_csv('tabla.csv',columns=['CODIGO', 'PRODUCTO', 'CANTIDAD'], index=False)
    productsList = productsList.as_matrix(columns=['CODIGO', 'PRODUCTO', 'CANTIDAD'])
    return productsList

def show_best_clients():
    '''
    Muestra los clientes que mas plata gastaron
    Returns: objeto iterable con los resultados
    '''
    df = pd.read_csv(STORE_DATA)
    df['TOTALGASTADO'] = df['CANTIDAD']*df['PRECIO']
    clientsList = df.groupby(by=['CLIENTE'], as_index=False).sum()
    clientsList = clientsList.sort_values(by=['TOTALGASTADO'])
    clientsList = clientsList.tail(5).iloc[::-1]
    clientsList.to_csv('tabla.csv',columns=['CLIENTE', 'TOTALGASTADO'], index=False)
    clientsList = clientsList.as_matrix(columns=['CLIENTE', 'TOTALGASTADO'])
    return clientsList