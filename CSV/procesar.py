try:
    open('ventas.csv').close()
except FileNotFoundError:
    print('El archivo no existe.')
    
with open('ventas.csv') as archivo:
    linea = archivo.readline().strip().split(',')
    headers = ['CODIGO', 'PRODUCTO', 'CLIENTE', 'CANTIDAD', 'PRECIO']
    '''Me guardo la posicion de la columna en el archivo
       segun el orden puesto en la lista headers'''
    col1 = linea.index(headers[0])
    col2 = linea.index(headers[1])
    col3 = linea.index(headers[2])
    col4 = linea.index(headers[3])
    col5 = linea.index(headers[4])
    
    '''Manejo de errores'''
    n = 0
    for l in archivo:
        lista = l.strip().split(',')
        n += 1
        if len(lista) != 5:
            raise Exception('La linea {} tiene un numero'
                            ' invalido de campos'.format(n))
        if lista[col1] == '':
            raise Exception('El campo CODIGO de la linea {}'
                            ' esta vacio'.format(n))
        try:
            int(float(lista[col4]))
        except ValueError:
            raise Exception('El campo CANTIDAD de la linea {}'
                            ' no es un numero entero'.format(n))
        try:
            float(lista[col5])
        except ValueError:
            raise Exception('El campo PRECIO de la linea {}'
                            ' no es un valor decimal'.format(n))
        