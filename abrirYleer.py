# Abrir y leer el archivo 
x = input("Ingrese el nombre del archivo: ")
with open(x) as archivo:
    for linea in archivo:
        lista = linea.split(",")
        # Sin conocer cant de columnas
        for i in lista:
            if "\n" in i:
                print(i, end="")
            else:
                print(i, end="\t")
        
        # Conociendo cant de columnas
        col1 = lista[0].strip()
        col2 = lista[1].strip()
        col3 = lista[2].strip() if not valores[3] is '' else '????-??-??'
        col4 = lista[3].strip()
        print("{:6}", col1)