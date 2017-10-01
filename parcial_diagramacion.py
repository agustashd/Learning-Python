
alumnos = []
for i in range(3):
	notas = []
	for j in range(3):
		x = int(input("Ingrese nota del alumno " + str(i + 1) + ": "))
		notas.append(x)
	alumnos.append(notas)

for i in range(len(alumnos)):
	promedio = 0
	for j in range(3):
		promedio += alumnos[i][j]
	promedio = promedio / 3
	if promedio < 4:
		print(i, ": DESAPROBO")
	else:
		print(i, ": ", promedio)
