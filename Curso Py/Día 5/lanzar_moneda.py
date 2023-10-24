from random import *


lista_numeros =[1,2,3,4,5]

def lanzar_moneda():
    moneda = ['Cara','Cruz']
    
    return choice(moneda)


def probar_suerte(lanzamiento,lista):
    
    if lanzamiento == 'Cara':
        print(f"La lista se autodestruirá")
        lista.clear()
        print(lista)
        return lista
    else:
        print(f"La lista fue salvada")
        print(lista)
        return lista
    
    
lanzamiento = lanzar_moneda()
jugada =probar_suerte(lanzamiento,lista_numeros)
    