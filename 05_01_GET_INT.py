# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

# Forma recursiva:
# la funcion se llama a sí misma en caso de que se lance una excepción ValueError, lo que permite al usuario volver a intentarlo hasta que ingrese un valor válido.

def get_int():
    try:
        value = int(input("Ingrese un valor entero: "))
        return value
    except ValueError:
        print("El valor ingresado no es un entero válido. Inténtelo nuevamente.")
        return get_int()

# Llamada a la función
resultado = get_int()
print("Valor entero ingresado:", resultado)