'''
Devuelva la cantidad de numeros pares dados
en una lista. Ej:
contar_pares([2, 1, 2, 3, 4]) -> 3
contar_pares([2, 2, 0]) -> 3
contar_pares([1, 3, 5]) -> 0
'''
def contar_pares(lista):
    x = 0
    for i in lista:
        if(i % 2 == 0):
            x+= 1
    return x

print(contar_pares([1, 3, 5]))