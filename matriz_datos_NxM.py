#!/usr/bin/env python3

"""Ingresar N lotes de M datos.
Calcule el promedio de cada lote e infórmelo en pantalla. Además muestre el 
dato máximo y el promedio mínimo y a qué número de lote pertenece cada uno.
"""


def carga_matriz(cant_lotes, cant_datos):
    "Función que sirve para cargar la matriz de NxM."

    matriz = []

    for i in range(cant_lotes):
        lote = []
        for j in range(cant_datos):
            dato = int(input('Ingrese el dato: '))
            lote.append(dato)
        matriz.append(lote)

    return matriz


def calcule_promedios(matriz):
    """Función que recibe una matriz y devuelve una lista con los promedios de 
    cada fila""" 

    promedios = []

    for lote in matriz:
        promedio = 0
        for item in lote:
            promedio = promedio + item
        promedio = promedio / len(lote)
        promedios.append(promedio)
    
    return promedios


def busca_maximo(matriz):
    """Función que busca el máximo de una matriz y devuelve ese valor y al último
    lote al que pertence."""

    maximo = matriz[0][0]
    nro_lote = 0

    for i, lote in enumerate(matriz):
        for valor in lote:
            if valor > maximo:
                maximo = valor
                nro_lote = i + 1 

    return maximo, nro_lote


def busca_minimo(lista):
    "Función que busca y devuelve el valor mínimo de una lista."

    minimo = lista[0]
    lote = 0

    for i, item in enumerate(lista):
        if item < minimo:
            minimo = item
            lote = i

    return minimo, lote + 1


if __name__ == '__main__':
    N = int(input('Cantidad de lotes a ingresar (N): '))
    M = int(input('Cantidad de datos por lote (M): '))

    matriz_datos = carga_matriz(cant_lotes=N, cant_datos=M)
    promedios = calcule_promedios(matriz=matriz_datos)

    print('Los promedios son: ')
    for promedio in promedios:
        print(promedio)

    dato_maximo, lote_dato_max = busca_maximo(matriz=matriz_datos)
    print('El dato ingresado máximo es: ', dato_maximo)
    print('\tY pertenece al lote N°: ', lote_dato_max)

    promedio_minimo, lote_promedio_min = busca_minimo(lista=promedios)
    print('El promedio mínimo es vale ', promedio_minimo)
    print('\tY pertenece al lote ', lote_promedio_min)
