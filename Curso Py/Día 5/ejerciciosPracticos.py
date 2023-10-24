def devolver_distintos(a,b,c):
    suma = a+b+c
    lista =[a,b,c]
    
    numero_mayor =  max(lista)
    numero_menor = min(lista)
    
    if suma > 15:
        return numero_mayor
    elif suma < 10:
        return numero_menor
    else:
        lista.sort()
        return lista[1]
        
        
#print(devolver_distintos(7,2,4))


def orden_alfabetico(palabra):
    mi_set = set()
    
    for letra in palabra:
        mi_set.add(letra)
    
    mi_lista = list(mi_set)
    mi_lista.sort()
    
    return mi_lista


#print(orden_alfabetico("entretenido"))


def cantidad_indefinidad(*args):
    
    contador =0
    
    for n in args:
        
        if contador +1  == len(args):
            return False
        
        elif args[contador]== 0 and args[contador+1] == 0:
            return True
        else:
            contador+=1
            
    return False

##print(cantidad_indefinidad(5,6,7,0,0,10,11,12))


def contar_primos(num):
    primos =[2]
    iteracion = 3
    
    if num < 2:
        return 0
    
    while iteracion <= num:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion+=2
                break
        else:
            primos.append(iteracion)
            iteracion+=2
                
    print(primos)
    return len(primos)

print(contar_primos(2500000))