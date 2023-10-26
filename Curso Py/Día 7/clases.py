class Casa:
    
    def __init__(self,color,cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


class Cubo:
    def __init__(self,color):
        self.caras = 6
        self.color = color
        
class Personaje:
    def __init__(self,especie,magico,edad):
        self.real = False
        self.especie = especie
        self.magico = magico
        self.edad = edad
        
harry_potter = Personaje("Humano",True,17)




cubo_rojo = Cubo("Rojo")

print(cubo_rojo.color)
print(cubo_rojo.caras)


casa_balanca = Casa('blanco',4)



print(f'Mi casa es de color {casa_balanca.color} y tiene {casa_balanca.cantidad_pisos} pisos')