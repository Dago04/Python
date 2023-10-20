palabra = "python"

lista = [letra for letra in palabra]

print(lista)



valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrados = [n**2 for n in valores]

print(valores_cuadrados)


valores = [1, 2, 3, 4, 5, 6, 9.5] 

valores_pares = [n for n in valores if n%2 == 0 ]

print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]


grados_celsius = [(grados_fahrenheit-32)*(5/9) for grados_fahrenheit in temperatura_fahrenheit]

print(grados_celsius)
