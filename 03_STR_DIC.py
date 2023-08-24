# 3 . Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia)
def contador(cadena):
    palabras = cadena.split()  # Dividir la cadena en palabras
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

entrada = input(str("Ingrese un texto: "))
resultado = contador(entrada)

print("Frecuencia de palabras:")
for palabra, frec in resultado.items():
    print(f"'{palabra}': {frec}")