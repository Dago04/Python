import random


def adivina_el_numero(x):
    
    
    print("==========================")
    print(" !Bienvenido(a) al Juego! ")
    print("==========================")
    print("Tu meta es adivinar el numero generado por la computadora.")
    
    numero_aleatorio = random.randint(1,x) #numero random entre 1 y x
    
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un númeor entre 1 y {x}: ")) #f-string
        
        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este número es menor que el número aleatorio")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este número es mayor que el número aleatorio")
        
    print(f"Felicitaciones! Has adivinado el número aleatorio {numero_aleatorio} correctamente")


adivina_el_numero(50)       
    
 