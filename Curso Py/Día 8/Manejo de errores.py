def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1+n2)
    print("Gracias por sumar" + n1)


try:
    # codigo que queremos probar
    suma()
except TypeError:
    # Codigo a ejecutar si hay un error
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un número")
else:
    # codigo a ejecturar sino hay un error
    print("Hiciste todo bien")
finally:
    # codigo que se va a ejecutar de todos modos
    print("Eso fue todo")


'''
def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero"))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break

    print("Gracias")


pedir_numero()
'''

# Ejercicio 1


def suma(num1, num2):
    try:
        suma = num1+num2
    except:
        print("Error inesperado")
    else:
        print(suma)
# suma(1, 2)


# Ejercicio 2

def cociente(num1, num2):
    try:
        cociente = num1/num2
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
    else:
        print(cociente)


# cociente(5, 5)

def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
        print(archivo.read())
    finally:
        print("Finalizando ejecución")
        archivo.close()


abrir_archivo('errores.txt')
