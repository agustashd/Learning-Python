class Corcho:
    '''Crea un corcho, atributo bodega'''

    def __init__(self, bodega):
        self.bodega = bodega
    
    def __str__(self):
        return 'Corcho de la beodega {}'.format(self.bodega)

class Botella:
    '''Crea una botella, atributo objeto Corcho o
       None si no se pasa argumento'''

    def __init__(self, corcho = None):
        if corcho != None:
            self.corcho = corcho.bodega
        else:
            self.corcho = None
    
    def __str__(self):
        if self.corcho:
            return 'Botella de la bodega {}'.format(self.corcho)
        else:
            return 'Soy una botella sin corcho'
    
class Sacacorchos:
    '''Crea un sacacorchos, un'''

    def __init__(self):
        self.corcho = False
        self.corcho_bodega = ""

    def __str__(self):
        if self.corcho == True:
            return 'Soy un sacacorchos y estoy ocupado'
        else:
            return 'Soy un sacacorchos y estoy libre'

    def destapar(self, botella):
        if botella.corcho == None or self.corcho == True:
            raise Exception('La botella esta destapada o el sacacorchos esta ocupado')
        else:
            self.corcho = True
            self.corcho_bodega = botella.corcho
            return 'Botella destapada!'
    
    def limpiar(self):
        if self.corcho == True:
            self.corcho = False
            self.corcho_bodega = ""
            return 'Listo para volver a ser usado!'
        else:
            raise Exception('No tengo un corcho, ¿que queres sacar?')

'''
c = Corcho("Catenas")
miBotella = Botella()
tuBotella = Botella(c)
print(miBotella)
print(miBotella.corcho)
print(tuBotella)
print(tuBotella.corcho)
saca = Sacacorchos()
#print(saca.destapar(miBotella)) '''tira la excepcion'''
print(saca.destapar(tuBotella))
print(saca.corcho_bodega)
print(saca)
print(saca.limpiar())
print(saca)
'''