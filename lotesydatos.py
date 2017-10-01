# Ingresar N lotes de M datos. Calcule el promedio
# de cada lote e informe el promedio de cada lote,
# eo dsto maximo y a que lote pertenece, y el
# promedio mas bajo y a que lote pertenece.

lotes = int(input("Ingrese la cantidad de lotes: "))
datos = int(input("Ingrese la cantidad de datos por lote: "))
matriz = []
for i in range(lotes):
    lote = []
    print("Ingrese los datos del lote ", i + 1, ": ")
    for j in range(datos):
        lote.append(int(input()))    	
    matriz.append(lote)
print(matriz)
# guardo promedio en una lista
