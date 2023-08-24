#7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:  Un constructor, donde los datos pueden estar vacíos.  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.  mostrar(): Muestra los datos de la cuenta.  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad debe ser un valor positivo.")
    
    def get_edad(self):
        return self.__edad
    
    def set_dni(self, dni):
        if len(dni) == 9:
            self.__dni = dni
        else:
            print("El DNI debe tener 9 caracteres.")
    
    def get_dni(self):
        return self.__dni
    
    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("DNI:", self.__dni)
    
    def es_mayor_de_edad(self):
        return self.__edad >= 18

class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad
    
    def set_titular(self, titular):
        self.__titular = titular
    
    def get_titular(self):
        return self.__titular
    
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
    
    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print("Titular:")
        self.__titular.mostrar()
        print("Cantidad:", self.__cantidad)
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad

# Crear una instancia de la clase Persona
titular = Persona("Juan", 30, "123456789")

# Crear una instancia de la clase Cuenta
cuenta = Cuenta(titular, 1000.0)

# Mostrar los datos de la cuenta
cuenta.mostrar()

# Ingresar dinero en la cuenta
cuenta.ingresar(500.0)

# Retirar dinero de la cuenta
cuenta.retirar(200.0)

# Mostrar los datos actualizados de la cuenta
cuenta.mostrar()
