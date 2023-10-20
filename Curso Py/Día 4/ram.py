from random import *

aleatorio = randint(1,50)
aleatorio = round(uniform(1,5),1) #arroja numeros con decimales
aleatorio =round(random(),1) #numeros aleatorios desde el 0 hasta el 1
colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores) #para elegir un item dentro de un list aleatorio

numeros = list(range(5,50,5))
shuffle(numeros) #shuffle no se puede usar con strings
print(numeros) 
print(aleatorio)
