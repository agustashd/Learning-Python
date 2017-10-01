'''
Implementar las eliminaciones del primero, uno
del medio y el ultimo elemento
Tambien implimentar una Pila y una Cola
'''
class ListaEnlazada:
    '''
    Crea la lista enlazada
    nodo: Nodo(valor, enlace)
    '''
    def __init__(self, nodo = None):
        self.nodo = nodo
    '''
    def __str__(self):
        return self.nodo
    '''    
    def agregar_valor(self, valor):
        nuevo_nodo = Nodo(valor, None)
        if self.nodo is None:
            self.nodo = nuevo_nodo
        else:
            aux = self.nodo
            while aux.enlace is not None:
                aux = aux.enlace
            aux.enlace = nuevo_nodo

class Nodo:
    '''
    Crea un nodo
    valor: dato a almacenar
    enlace: nombre del Nodo() siguiente
    '''
    def __init__(self, valor, enlace):
        self.valor = valor
        self.enlace = enlace
    
    def __str__(self):
        return str(self.valor)

