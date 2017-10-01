'''
Dadas 2 listas de enteros, devuelva True si
ambas comienzan con el mismo elemento o si
terminan con el mismo elemento. Ej:
mismo_extremo([1, 2, 3], [7, 3]) -> True
mismo_extremo([1, 2, 3], [7, 3, 2]) -> False
mismo_extremo([1, 2, 3], [1, 3]) -> True
'''
def mismo_extremo(lista1, lista2):
    if (lista1[0] == lista2[0] or lista1[-1] == lista2[-1]):
        return True
    return False

print(mismo_extremo([1, 2, 3], [1, 3]))