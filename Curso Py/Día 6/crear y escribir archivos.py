archivo = open('prueba.txt', 'a')  #'a' abrir el archivo en la ultima linea del texto
archivo.write('Soy el nuevo texto xd\n')
archivo.write('Hola mundo\n')
archivo.write('''Dagoberto
Salas
Cordero''')

archivo.writelines(['Hola','Mundo','Acá','Estoy']) # escribir string uno detra de otro


lista = ['Hola','Mundo','Acá','Estoy']

for p in lista:
    archivo.write(p + '\n')

archivo.close()