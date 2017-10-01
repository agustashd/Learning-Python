'''
Ejercicio 15.5.1. Papel, Birome, Marcador
a) Escribir una clase Papel que contenga un texto, un método escribir,
que reciba una cadena para agregar al texto, y el método __str__ 
que imprima el contenido del texto.
b) Escribir una clase Birome que contenga una cantidad de tinta,
y un método escribir, que reciba un texto y un papel sobre el cual
escribir. Cada letra escrita debe reducir la cantidad de tinta contenida.
Cuando la tinta se acabe, debe lanzar una excepción.
c) Escribir una clase Marcador que herede de Birome, y agregue el 
método recargar, que reciba la cantidad de tinta a agregar.
'''
class Papel:
    '''
    Papel contiene un texto y un metodo escribir para agregar mas texto
    texto: string
    '''
    def __init__(self, texto = ''):
        self.texto = texto

    def __str__(self):
        return self.texto

    def escribir(self, texto):
        self.texto += texto

class NoMoreInkError(Exception):
    pass

class Birome:
    '''
    Birome contiene una cantidad y un metodo para ecribir sobre un Papel
    a partir de un texto
    cantidad_tinta: int
    '''
    def __init__(self, cantidad_tinta = 300):
        self.cantidad_tinta = cantidad_tinta

    def __str__(self):
        return 'Tengo {} caracteres de tinta disponible'.format(
        self.cantidad_tinta
        )

    def escribir(self, papel, texto):
        for caracter in texto:
            if self.cantidad_tinta > 0:
                papel.escribir(caracter)
                self.cantidad_tinta -= 1
            else:
                print(papel)
                raise NoMoreInkError('Se acabo la tinta!')

class Marcador(Birome):
    '''
    Marcador hereda de Birome y puede cargar tinta
    cantidad_tinta: int
    '''
    def __init__(self, cantidad_tinta = 200):
        super().__init__(cantidad_tinta)

    def recargar(self, tinta):
        self.cantidad_tinta += tinta

'''
hoja = Papel('Hola guacho')
birome = Birome(20)
print(hoja)
birome.escribir(hoja, ' mira como escribo aca')
print(birome)
marcador = Marcador()
print(marcador)
marcador.recargar(300)
print(marcador.cantidad_tinta)
'''