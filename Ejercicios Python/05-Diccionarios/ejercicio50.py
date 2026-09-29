estudiantes = {}

cantidad = int(input("Ingrese la cantidad de estudiantes: "))

for i in range(cantidad):
    codigo = input("Ingrese el código del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    carrera = input("Ingrese la carrera del estudiante: ")
    promedio = float(input("Ingrese el promedio del estudiante: "))

    estudiantes[codigo] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "promedio": promedio
    }

mayor = 0
codigo_estudiante = ""

for codigo, datos in estudiantes.items():
    if datos["promedio"] > mayor:
        mayor = datos["promedio"]
        codigo_estudiante = codigo

print("Mejor estudiante")
print("Código:", codigo)
print("Nombre:", estudiantes[codigo_estudiante]["nombre"])
print("Edad:", estudiantes[codigo_estudiante]["edad"])
print("Carrera:", estudiantes[codigo_estudiante]["carrera"])
print("Promedio:", estudiantes[codigo_estudiante]["promedio"])