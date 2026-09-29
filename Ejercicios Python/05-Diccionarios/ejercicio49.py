empleados = {}

cantidad = int(input("Ingrese la cantidad de empleados: "))

suma = 0

for i in range(cantidad):
    identificacion = input("Ingrese el número de identificación: ")
    salario = float(input("Ingrese el salario: "))

    empleados[identificacion] = salario
    suma = suma + salario

promedio = suma / cantidad

print(f"El salario promedio es: ${promedio:.2f}")