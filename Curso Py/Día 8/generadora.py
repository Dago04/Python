'''def mi_función():
    lista = []
    for x in range(1, 5):
        lista.append(x)
    return lista


def mi_generador():
    for x in range(1, 5):
        yield x * 10


print(mi_función())


g = mi_generador()
print(next(g))
print(next(g))
'''


'''def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


generador = mi_generador()

print(next(generador))
print(next(generador))

print(next(generador))
'''

# Definición del generador

# ejercicio 1


def numeros_infinitos():
    numero = 1
    while True:
        yield numero
        numero += 1


# Creación de una instancia del generador
generador = numeros_infinitos()


print(next(generador))

# ejercicio 2


def multiplo():
    contador = 7
    while True:
        yield contador
        contador += 7


generador = multiplo()


# ejercicio 3
def generador_perder_vida():
    vidas = 3
    while vidas > 0:
        yield f"Te quedan {vidas} vidas"
        vidas -= 1

    if vidas <= 0:
        print("Game Over")


perder_vida = generador_perder_vida()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
