libros = {}

cantidad = int(input("Ingrese la cantidad de libros: "))

for i in range(cantidad):
    codigo = input("Ingrese el código del libro: ")
    titulo = input("Ingrese el título del libro: ")

    libros[codigo] = titulo

buscar = input("Ingrese el código del libro que desea consultar: ")

if buscar in libros:
    print("Libro encontrado:")
    print(buscar, "->", libros[buscar])
else:
    print("El libro no se encuentra registrado.")