palabra = input("Ingrese una palabra: ")

letras = {}

for letra in palabra:
    if letra in letras:
        letras[letra] = letras[letra] + 1
    else:
        letras[letra] = 1

for letra, cantidad in letras.items():
    print(letra, ":", cantidad)