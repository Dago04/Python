class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"Pio, mi color es {self.color}")

    def volar(self, metros):
        print(f"El pajaron ha volado {metros} metros")


class Mago:
    def __init__(self, nombre):
        self.nombre = nombre

    def lanzar_hechizo(self):
        print(f"El mago {self.nombre} ha lanzado el hechizo ¡Abracadabra!")


merlin = Mago("Merlin")

merlin.lanzar_hechizo()


class Alarma:
    def __init__(self, nombre):
        self.nombre = nombre

    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido postergada {cantidad_minutos} minutos")


alarma = Alarma("nelson")

alarma.postergar(5)
