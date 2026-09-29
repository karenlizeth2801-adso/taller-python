frase = input("Ingrese una frase: ")

contador = {}
palabra = ""

for letra in frase:
    if letra != " ":
        palabra = palabra + letra
    else:
        if palabra in contador:
            contador[palabra] = contador[palabra] + 1
        else:
            contador[palabra] = 1

        palabra = ""

if palabra in contador:
    contador[palabra] = contador[palabra] + 1
else:
    contador[palabra] = 1

for palabra, cantidad in contador.items():
    print(palabra, ":", cantidad)