#4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def contador(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
            
    return frecuencia

def palabra_tupla(diccionario):
    frecuencia_tupla = 0
    palabra_tupla = ""
    
    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_tupla:
            frecuencia_tupla = frecuencia
            palabra_tupla = palabra
            
    return (palabra_tupla, frecuencia_tupla)

cadena_input = input(str("Ingrese una cadena de caracteres: "))
resultado = contador(cadena_input)

print("Frecuencia de palabras:")
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")

resultado_tupla = palabra_tupla(resultado)
print("Palabra más repetida:", resultado_tupla[0])
print("Frecuencia:", resultado_tupla[1])

