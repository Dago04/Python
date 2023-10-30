class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")


class Pajaro(Animal):
    pass


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Alumno(Persona):
    pass


class Vehiculo:
    @classmethod
    def acelerar(cls):
        pass

    @classmethod
    def frenar(cls):
        pass


class Automovil(Vehiculo):
    pass


carro = Automovil()

carro.acelerar()
carro.frenar
