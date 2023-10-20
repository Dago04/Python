
def chequear_3_cifras(lista):
    
    lista_3_cifras=[]
    
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras


resultado = chequear_3_cifras([555,99,600])

print(resultado)



#Ejercicio 1
lista_numeros = [-1,-5,2]
def todos_positivos(lista):

    for n in lista_numeros:
        if n>0:
            return True
        else:
            pass
    return False


resul = todos_positivos(lista_numeros)
print(resul)

#Ejercicio 2

lista_numeros= list(range(-50,2000))


def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n > 0 and n < 1000:
            suma+=n
        else:
            pass
    return suma
    
resultado = suma_menores(lista_numeros)
print(resultado)
    
#Ejercicio 3


def cantidad_pares(lista):
    cantidad_pares = 0
    for i in lista_numeros:
        if i%2 == 0:
            cantidad_pares+=1
        else:
            pass
    return cantidad_pares
lista_numeros = list(range(1,50))
resul1 = cantidad_pares(lista_numeros)
print(resul1)



#Ejercicio 4


def cantidad_pares(lista):
    cantidad_pares = 0
    cantidad_impares = 0
    for i in lista_numeros:
        if i%2 == 0:
            cantidad_pares+=1
        else:
            cantidad_impares+=1
    return cantidad_pares,cantidad_impares
lista_numeros = list(range(1,51))
resul1 = cantidad_pares(lista_numeros)
print(resul1)

        
