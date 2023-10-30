class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"Pio, mi color es {self.color}")

    def volar(self, metros):
        print(f"El pajaron ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos y el pajara se llama{cls.pintar_negro()}")

    @staticmethod
    def mirar():
        print("El pajaro mira")


class Persona:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        vivo = True
        print(vivo)


Persona.respirar()

Jugador.revivir()
