lista = [1,2,3,4,5,6,7,8,9,10]

pares = []
inpares = []

for numeros in lista:
    if numeros%2 == 0:
        pares.append(numeros)
    elif numeros%1 == 0:
        inpares.append(numeros)

print(pares)
print(inpares)
        
