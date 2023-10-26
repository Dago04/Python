from pathlib import * 

carpeta = Path("C:/Users/Dago/Documents/GitHub/Python/Curso Py/Día 6/prueba.txt")

ruta_windows = PureWindowsPath(carpeta) #convertir ruta a una ruta de windows

if not carpeta.exists():
    print("Este archivo no existe")
else: 
    print("Existes")

print(carpeta.stem)#devuelve solo el nombre del archivo
print(carpeta.suffix) #devuelve el tipo del archivo
print(carpeta.name)#devuelve el nombre
print(carpeta.read_text())#lee el archivo

print(ruta_windows)