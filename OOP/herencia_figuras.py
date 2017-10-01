class Figura:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    def area(self):
        raise NotImplementedError("Este método debe ser redefinido.")
    def __str__(self):
        return "<{} - color: {} - área: {:.2f}>".format(
        self.nombre, self.color, self.area()
        )
    def __repr__(self):
        return "Forma: {} \nColor: {}\nArea: {}".format(
        self.nombre, self.color, self.area()
        )

class Circulo(Figura):
    from math import pi
    def __init__(self, radio, color):
        '''
        Circulo hereda de Figura y utlizando super()
        llamamos a los atributos y los redefinimos o
        seteamos segun querramos hacerlo
        '''
        super().__init__("Circulo", color)
        self.radio = radio
        
    
    def area(self):
        return pi * self.radio * self.radio

    