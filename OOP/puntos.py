class Punto:
    '''Representacion de un punto en
       coordenadas cartesianas (x, y)'''
    
    def __init__(self, x, y):
        '''Constructor de Punto. x e y deben ser numeros
           caso contrario se levanta una excepcion'''
        self.x = validar_numero(x)
        self.y = validar_numero(y)

    def distancia(self, otro):
        '''Devuelve la distancia entre ambos puntos'''
        return self.restar(otro).norma()

    def restar(self, otro):
        '''Devuelve el Punto que resulta de la resta
           entre dos puntos'''
        return Punto(self.x - otro.x, self.y - otro.y)

    def norma(self):
        '''Devuelve la norma del vector que va desde
           el origen hasta el punto'''
        return (self.x * self.x + self.y * self.y) ** 0.5
    
def validar_numero(valor):
    '''Si el valor es numerico, lo devuelve.
        En caso contrario lanza TypeError'''
    if not isinstance(valor, (int, float, complex)):
        raise TypeError(valor,' no es un valor numerico')
    return valor

p = Punto(5, 7)
q = Punto(2, 3)
r = p.restar(q)
print(q.norma())