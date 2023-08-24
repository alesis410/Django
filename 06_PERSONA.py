""" #6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad. """

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

# Crear una instancia de la clase Persona
persona = Persona()

# Establecer valores utilizando los setters
persona.set_nombre("Juan")
persona.set_edad(25)
persona.set_dni("123456789")

# Mostrar los datos de la persona
persona.mostrar()

# Verificar si es mayor de edad
if persona.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")