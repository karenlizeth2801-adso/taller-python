calificaciones = []

cantidad = int(input("Ingrese la cantidad de calificaciones: "))

suma = 0

for i in range(cantidad):
    nota = float(input("Ingrese una calificación: "))
    calificaciones.append(nota)
    suma = suma + nota

promedio = suma / cantidad

print(f"El promedio de las calificaciones es: {promedio:.2f}")
