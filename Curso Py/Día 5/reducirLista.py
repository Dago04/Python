
lista_numeros = [1,2,15,7,2,7,50]

def reducir_lista(lista):
    nueva_lista = []
  
    for numero in lista:
        if numero not in nueva_lista:
            nueva_lista.append(numero)
    
    nueva_lista.remove(max(nueva_lista))  
    return nueva_lista


def promedio(lista):
    suma =0
    promedio =0
    
    suma =sum(lista)
    
    promedio = suma / len(lista)

    print(f"El promedio de la lista es de {promedio}")
    

lista_reducida= reducir_lista(lista_numeros)
promedio_lista = promedio(lista_reducida)