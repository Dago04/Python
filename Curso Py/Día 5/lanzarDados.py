from random import *


def lanzar_dados():
    
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1,dado2


def evaluar_jugada(dado1,dado2):
    suma = dado1+dado2
    mensaje = ''
    
    if suma <= 6:
      mensaje = print(f"La suma de tus dados es {suma}. Lamentable")
    elif suma > 6 and suma <  10:
      mensaje = print(f"La suma de tus dados es {suma}. Tienes buenas chances")
    elif suma >= 10:
      mensaje =print(f"La suma de tus dados es {suma}. Parece una jugada ganadora")
    
    return mensaje

dado1, dado2 = lanzar_dados()

jugada = evaluar_jugada(dado1,dado2)




