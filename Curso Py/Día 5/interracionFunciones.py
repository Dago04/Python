from random import *


palitos = ['-','--','---','----']


#Mezclar palitos
def mezclar_palitos(lista):
    shuffle(lista)
    return lista

#pedirle intento
def probar_suerte():
    intento = ''
    
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero entre el 1 y el 4: ")
        
    return int(intento)


#comprobar intento
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Te has salvado")
        
    print(f"Te ha tocado {lista[intento-1]}")
    
    

palitos_mezclados = mezclar_palitos(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)