#Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).

def abrir_leer(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return "El archivo no se encontró."
    except Exception as e:
        return f"Ocurrió un error: {str(e)}"

# Ejemplo de uso:
nombre_archivo = "texto.txt"
contenido = abrir_leer(nombre_archivo)
if contenido:
    print("Contenido del archivo:")
    print(contenido)
    
#Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

def sobrescribir(nombre_archivo):
    with open(nombre_archivo, 'w') as documento:
        contenido = documento.write("contenido eliminado")
        documento.close()
    return print("Se ha eliminado el contenido del documento "+ documento.name)

nombre_archivo = "texto.txt"
contenido = abrir_leer(nombre_archivo)


#Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, 
# y lo actualice añadiendo una línea al final que indique 
# "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.

def registro_error(archivo):
    with open(archivo,'a') as documento:
        documento.write("se ha registrado un error de ejecución")
        documento.close()
        