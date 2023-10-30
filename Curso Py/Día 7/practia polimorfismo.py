class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


mago1 = Mago()
arquero1 = Arquero()
samurai1 = Samurai()


personajes = [arquero1, mago1, samurai1]

for personaje in personajes:
    personaje.atacar()
