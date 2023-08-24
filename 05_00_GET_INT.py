# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

# Forma iterativa:
# se utiliza un bucle while que continúa pidiendo al usuario que ingrese un valor hasta que se proporcione un valor entero válido

def get_int():
    while True:
        try:
            value = int(input("Ingrese un valor entero: "))
            return value
        except ValueError:
            print("El valor ingresado no es un entero válido. Inténtelo nuevamente.")


resultado = get_int()
print("Valor entero ingresado:", resultado)


