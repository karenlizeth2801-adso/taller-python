estudiantes = {}

cantidad = int(input("Ingrese la cantidad de estudiantes: "))

for i in range(cantidad):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota final: "))

    estudiantes[nombre] = nota

mayor = 0
mejor_estudiante = ""

for nombre, nota in estudiantes.items():
    if nota > mayor:
        mayor = nota
        mejor_estudiante = nombre

print("El estudiante con la mejor nota es:")
print(mejor_estudiante, "->", mayor)