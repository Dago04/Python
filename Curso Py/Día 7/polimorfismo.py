class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "dice muu")


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")


vaca1 = Vaca('Aurora')
oveja1 = Oveja('tu madre')

animales = [vaca1, oveja1]


def animal_hablar(animal):

    animal.hablar()


animal_hablar(oveja1)
