numeros = []

cantidad = int(input("Ingrese la cantidad de números: "))

for i in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
