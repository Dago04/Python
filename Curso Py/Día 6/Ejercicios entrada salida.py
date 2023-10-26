mi_archivo = open('texto.txt')


#leer todo el archivo
print(mi_archivo.read())


# leer primera linea
mi_archivo= open('texto.txt')

una_linea = mi_archivo.readline()

print(una_linea)


#Leer la segunda linea
mi_archivo= open('texto.txt')

lineas = mi_archivo.readlines()


print(lineas[1])