'''
-listar todos los productos que compro un cliente
-listar todos los clientes que compraron un determinado producto 
-listar los n productos mas vendidos
-listar los n clientes que mas plata gastaron
'''
def productosComprados(cliente):
    '''
    listar todos los productos comprados por cliente
    cliente: nombre del cliente tal cual figura en el csv
    '''
    try:
        open('ventas.csv').close()
    except FileNotFoundError:
        print('El archivo no existe.')

    with open('ventas.csv') as archivo:
        linea = archivo.readline().strip().split(',')
        regProducto = linea.index('PRODUCTO')
        regCliente = linea.index('CLIENTE')

        productos = []
        for registro in archivo:
            lista = registro.strip().split(',')
            if lista[regCliente] == cliente:
                productos.append(lista[regProducto])

        if productos == []:
            return 'El cliente no compro nada'
        else:
            return list(set(productos))

def clientesCompraron(producto):
    '''
    listar todos los clientes que compraron un determinado producto
    producto: nombre del producto tal cual figura en el csv
    '''
    try:
        open('ventas.csv').close()
    except FileNotFoundError:
        print('El archivo no existe.')

    with open('ventas.csv') as archivo:
        linea = archivo.readline().strip().split(',')
        regProducto = linea.index('PRODUCTO')
        regCliente = linea.index('CLIENTE')

        clientes = []
        for registro in archivo:
            lista = registro.strip().split(',')
            if lista[regProducto] == producto:
                clientes.append(lista[regCliente])

        if clientes == []:
            return 'El producto no fue comprado'
        else:
            return list(set(clientes))

print(productosComprados('CLIENTE PARTICULAR 00'))
print(clientesCompraron('CLONAPLEX 400 X12'))