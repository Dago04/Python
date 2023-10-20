numero = 50
while numero >= 0:
    numero -= 1
    if numero % 5 == 0:
        print(numero)
    else:
        continue
    
    
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numeros in lista_numeros:

    if numeros < 0:
        continue
    
    print(numeros)