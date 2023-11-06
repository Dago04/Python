from collections import Counter, defaultdict, namedtuple, deque

'''metodos de counter
split(), mostcommon() = ordena en tupla segun la aparicion mas frecuente

numeros = [8, 6, 4, 7, 8, 6, 1, 1, 2, 2, 3, 2, 5, 10]
serie = Counter([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 22, 2, 3,
                3, 3, 3, 3, 33, 3, 3, 33, 3, 3, 3])

print(serie.most_common())
print(list(serie))

# Count : contar numeros de una lista y devolverlos como un diccionario, tambien cuenta palabras
# con el metodo split cuenta las palabras repetidas
frase = 'al pan al pan y al vino vino'
coleccion = Counter(numeros)
print(Counter(frase.split()))

print(coleccion)'''


'''dic = defaultdict(lambda: 'nada')
dic['uno'] = 'verde'

print(dic['uno'])
'''

'''Persona = namedtuple('Persona', ['Nombre', 'Altura', 'Peso'])

ariel = Persona('Ariel', 1.90, 100)
print(ariel.Altura)
'''

lista_ciudades = deque(
    ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

# Agregar elementos al inicio de la deque
lista_ciudades.appendleft("Budapest")

'''# Agregar elementos al final de la deque
lista_ciudades.append("Atenas")

# Eliminar el primer elemento de la deque
lista_ciudades.popleft()

# Eliminar el último elemento de la deque
lista_ciudades.pop()'''

print(lista_ciudades)
