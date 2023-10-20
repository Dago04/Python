from random import *
intentos = 0
numero_usuario= 0
numero_aleatorio = randint(1,100)

nombre = input("Dime tu nombre: ")

print(f"Bueno,{nombre}, he pensado un numero entre 1 y 100, y tienes solo ocho intentos para adivinar")

while intentos < 8 :
    numero_usuario =int(input("Digite un numero a ver si adivinas: "))
    intentos +=1
    
    if numero_usuario < 1 or numero_usuario >100:
        print("Has elegido un numero que no esta permitido")
        
    elif numero_usuario < numero_aleatorio:
        print("Respuesta Incorrecta, has elegido un número menor al número secreto")
      
    elif numero_usuario > numero_aleatorio:
         print("Respuesta Incorrecta, has elegido un número mayor al número secreto")
     
    else:
        print(f"Felicidades has acertado el número secreto, solo te ha tomado {intentos} intentos!")
        break
if numero_usuario !=numero_aleatorio:
    print(f"Intentos agotados. El número secreto era {numero_aleatorio}")
 
        