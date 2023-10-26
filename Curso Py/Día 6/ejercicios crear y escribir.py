#Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
#Imprime el contenido completo de "mi_archivo.txt" al finalizar.

archivo = open('mi_archivo.txt','w')

archivo.write('Nuevo texto')

archivo.close()

archivo = open('mi_archivo.txt','r')
print(archivo.read())


#Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

#Imprime el contenido completo de "mi_archivo.txt" al finalizar.

archivo = open('mi_archivo.txt','a')

archivo.write('Nuevo inicio de sesión')

archivo.close()

archivo = open('mi_archivo.txt','r')
print(archivo)


registro_ultima_sesion = ["Federico\t","20/12/2021\t","08:17:32 hs\t","Sin errores de carga"]

#Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . 
# Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico\t","20/12/2021\t","08:17:32 hs\t","Sin errores de carga"]

archivo = open('registro.txt','a')

archivo.writelines(registro_ultima_sesion )

archivo.close()

archivo = open('registro.txt','r')

print(archivo.read())