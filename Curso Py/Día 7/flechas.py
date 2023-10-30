class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1
            print(
                f"¡Has lanzado una flecha! Ahora te quedan {self.cantidad_flechas} flechas.")
        else:
            print("¡No tienes flechas suficientes!")


# Prueba del método lanzar_flecha()
personaje1 = Personaje(5)
personaje1.lanzar_flecha()
personaje1.lanzar_flecha()
personaje1.lanzar_flecha()
