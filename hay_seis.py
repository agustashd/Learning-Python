'''
Dada una lista de enteros, devuelva True si
el '6' aparece al principio o al final de la
lista. Ej:
hay_seis([1, 2, 6]) -> True
hay_seis([6, 1, 2, 3]) -> True
hay_seis([5, 6, 1, 4, 3]) -> False
'''
def hay_seis(lista):
    if (lista[0] == 6 or lista[-1] == 6):
        return True
    return False

print(hay_seis([6, 1, 2, 3]))