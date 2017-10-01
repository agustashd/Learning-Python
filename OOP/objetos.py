class Mascota:
    tipo = "mascota"
    name = None
    edad = 0
    def __str__(self):
        return "Soy un {} y me llamo {}".format(self.tipo, self.name)
    def __repr__(self):
        return "Mascota"

class Carta:
    valor = 0
    palo = None