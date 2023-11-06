import os
import shutil
import send2trash
send2trash.send2trash('curso.txt')

# print(os.getcwd())  # nos muestra el directorio donde estamos


'''archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()'''

# print(os.listdir()) lista de los archivos en el directorio

# sirve para mover directorios
# shutil.move('curso.txt', "C:\\Users\\Dago\\Desktop")


# eliminar archivos
# os.unlink()  # eliminar y recibe un path
# os.rmdir()  # eliminar carpeta vacia
# shutil.rmtree()  # eliminar todo 'no usar'

print(os.walk())
