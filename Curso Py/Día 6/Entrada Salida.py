mi_archivo = open('prueba.txt')
todas = mi_archivo.readlines() # este metodo lo que ahce es meter cada linea en una lista
todas = todas.pop()

print(todas)

una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea.rstrip()) # rstrip() funciona para que no haga salto de linea al sobreescribir la siguiente linea

una_linea = mi_archivo.readline()
print(una_linea)



for l in mi_archivo:
    print("Aqui dice: "+l)



mi_archivo.close()