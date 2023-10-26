import os
from pathlib import *

 #os.getcwd() para traer el directorio donde esta el script de python 
 #os.chdir('C:\\Users\\Dago\\Documents\\GitHub\\Python\\Curso Py\\Día 6') sirve para cambiar de directorio
 #os.makedirs sirve para crear directorios(nueva carpeta)
 #os.path.basename devuelve el nombre del archivo de la ruta
 #os.path.dirname devuelve el nombre de la ruta
 #os.path.split devuelve en una tupla el nombre de la ruta y el nombre del archivo
 #os.rmdir = elimina el directorio que le pasemos
 
 #como usar hacer que cualquier usuario ya sea windows o mac pueden usar este archivo
carpeta = Path("C:/Users/Dago/Documents/GitHub/Python/Curso Py/Día 6")
archivo = carpeta / 'prueba.txt'

mi_archivo =  open(archivo)
print(mi_archivo.read())
 

