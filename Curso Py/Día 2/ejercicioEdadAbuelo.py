import datetime

anio_matrimonio = int(input("Digite el año de matrimono "))
fecha_actual = int(datetime.datetime.now().year)
edad_abuelo = fecha_actual-anio_matrimonio
edad_abuela = edad_abuelo-7

print("La edad de la abuela es de " + edad_abuela)