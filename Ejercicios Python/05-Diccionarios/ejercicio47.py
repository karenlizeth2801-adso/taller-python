ventas = {}

cantidad = int(input("Ingrese la cantidad de vendedores: "))

for i in range(cantidad):
    nombre = input("Ingrese el nombre del vendedor: ")
    venta = float(input("Ingrese el total vendido: "))

    ventas[nombre] = venta

mayor = 0
mejor_vendedor = ""

for nombre, venta in ventas.items():
    if venta > mayor:
        mayor = venta
        mejor_vendedor = nombre

print("Mayor vendedor:")
print(mejor_vendedor, "-> $", mayor)