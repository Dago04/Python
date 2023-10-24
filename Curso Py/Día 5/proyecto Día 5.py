from random import *

def palabra_oculta():
    palabra_oculta = ["dedos",'python','ahorcado','pediatra']
    
    return choice(palabra_oculta)


def inicializar_guiones(palabra):
    guiones = '-' * len(palabra)
    return guiones


def mostrar_progreso(palabra, guiones):
    for letra in guiones:
        print(letra, end=' ')
    print()


def juego_ahorcado():
    palabra_secreta = palabra_oculta()
    guiones = inicializar_guiones(palabra_secreta)
    intentos = 6
    
    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tienes {intentos} intentos para adivinar la palabra.")
    mostrar_progreso(palabra_secreta, guiones)
    
    
    while intentos > 0 and '-' in guiones:
        letra = input("Ingresa una letra: ").lower()
        
        if len(letra)!=1 or not letra.isalpha():
            print("Ingresa una letra valida.")
            continue
        
        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    guiones = guiones[:i] + letra + guiones[i+ 1:]
        else:
            intentos-=1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")
            
        mostrar_progreso(palabra_secreta, guiones)
    
    if '-' not in guiones:
        print(f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
    else:
        print(f"¡Perdiste! La palabra secreta era: {palabra_secreta}")

juego_ahorcado()

