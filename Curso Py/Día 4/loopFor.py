lista = ['a','b','c']

for letra in lista:
    numero_letra = lista.index(letra) +1    
    print(f"Letra {numero_letra}: {letra}")
    

lista2= ['pablo','laura','dago','pablo','laureano']
lista2.sort()

for nombre in lista2:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print(f"Nombres que no comienzan con L: {nombre}")
        
numeros =[1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor+numero
    
print(mi_valor)

palabra = "python"

for letra in palabra:
    print(letra)
    
    


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numeros in lista_numeros:
    suma_numeros= suma_numeros+numeros

print(suma_numeros)


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numeros in lista_numeros:
    if numeros%2 == 0:
        suma_pares = suma_pares+numeros
    elif numeros%2 ==1:
        suma_impares = suma_impares+numeros


print(suma_pares)
print(suma_impares)

