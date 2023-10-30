class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelvo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")


class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def reir(self):
        print("ja ja")

    def hablar(self):
        print("Qué tal")


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()

mi_nieto.hablar()


class Vertebrado:
    vertebrado = True


class Ave(Vertebrado):
    tiene_pico = True

    def poner_huevos(self):
        print("Poniendo huevos")


class Reptil(Vertebrado):
    venenoso = True


class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")

    def poner_huevos(self):
        print("Poniendo huevos")


class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")

    def amamantar(self):
        print("Amamantando crías")


class Ornitorrinco(Pez, Reptil, Ave, Mamifero):
    pass


ornitorrinco = Ornitorrinco()
ornitorrinco.nadar()  # Output: Nadando
ornitorrinco.poner_huevos()  # Output: Poniendo huevos
ornitorrinco.caminar()  # Output: Caminando
ornitorrinco.amamantar()  # Output: Amamantando crías
print(ornitorrinco.tiene_pico)  # Output: True
print(ornitorrinco.vertebrado)  # Output: True
print(ornitorrinco.venenoso)  # Output: True
