class Hotel:
    '''Representa un hotel: sus atributos son:
       nombre, ubicacion, puntaje y precio'''

    def __init__(self, nombre, ubicacion, puntaje, precio):
        '''Crea un hotel
           Nombre y ubicacion deben ser no vacios y puntaje
           y precio numeros positivos. Sino se levanta una excepcion'''
        self.nombre = validar_cadena_no_vacia(nombre)
        self.ubicacion = validar_cadena_no_vacia(ubicacion)
        self.puntaje = validar_numero_positivo(puntaje)
        self.precio = validar_numero_positivo(precio)

    def __str__(self):
        '''Conversion a cadena de texto'''
        return '{} de {} - Puntaje: {} - Precio: {} pesos'.format(
                self.nombre,
                self.ubicacion,
                self.puntaje,
                self.precio)
    
    def __lt__(self, otro):
        '''Compara dos hoteles segun sus ratios'''
        return self.ratio() < otro.ratio()

    def ratio(self):
        '''Calcula calidad/precio'''
        return (10 * self.puntaje * self.puntaje) / self.precio


def validar_cadena_no_vacia(cadena):
    '''Si la cadena es no vacia la devuelve,
       en caso contrario TypeError'''
    if cadena == "":
        raise TypeError('Ingreso una cadena vacia')
    return cadena

def validar_numero_positivo(valor):
    '''Si el valor es positivo lo devuelve,
       en caso contrario TypeError'''
    if valor < 0:
        raise TypeError('Ingreso un valor negativo')
    return valor

h1 = Hotel("Hotel City", "Mercedes", 3.25, 78)
h2 = Hotel("Hotel Mascardi", "Bariloche", 6, 150)
h3 = Hotel("Hotel Cas", "Mercedes", 3.8, 85)
h4 = Hotel("Hotel Mas", "Bariloche", 6.5, 100)
lista = [h1, h2, h3, h4]

def precio(hotel):
    return hotel.precio

lista.sort(key=precio)

print(h1)
print(h1.ratio())
print(h2 < h1)
for hotel in lista:
    print(hotel)