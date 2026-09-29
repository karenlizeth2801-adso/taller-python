agenda = {}

cantidad = int(input("Ingrese la cantidad de contactos: "))

for i in range(cantidad):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")

    agenda[nombre] = telefono

buscar = input("Ingrese el nombre del contacto que desea buscar: ")

if buscar in agenda:
    print("Teléfono de", buscar, ":", agenda[buscar])
else:
    print("El contacto no se encuentra en la agenda.")