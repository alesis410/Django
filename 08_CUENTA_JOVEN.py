#8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:  Un constructor.  Los setters y getters para el nuevo atributo.  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.


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

class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    def set_bonificacion(self, bonificacion):
        if bonificacion >= 0:
            self.__bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.__bonificacion
    
    def es_titular_valido(self):
        if self.get_titular().es_mayor_de_edad() and self.get_titular().get_edad() < 25:
            return True
        return False
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero, el titular no es válido.")
    
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación:", self.__bonificacion)

# Crear una instancia de la clase Persona
titular_joven = Persona("María", 22, "987654321")

# Crear una instancia de la clase CuentaJoven
cuenta_joven = CuentaJoven(titular_joven, 800.0, 5.0)

# Mostrar los datos de la cuenta joven
cuenta_joven.mostrar()

# Intentar retirar dinero siendo titular válido
cuenta_joven.retirar(100.0)

# Cambiar el titular a uno no válido (mayor de 25 años)
titular_joven.set_edad(26)
cuenta_joven.set_titular(titular_joven)

# Intentar retirar dinero siendo titular no válido
cuenta_joven.retirar(50.0)
