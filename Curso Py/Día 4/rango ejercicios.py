mi_lista = [num for num in range(3, 301) if num % 3 == 0]

print(mi_lista)

suma_cuadrados = 0

for numero in range(1,16):
    
    suma_cuadrados += numero**2
    print(suma_cuadrados)