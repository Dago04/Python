if 10>9:
    print('Es correcto')
else:
    print('10 no es mayor que 9')
    
mascota ='perro'

if mascota == 'gato':
    print("Tienes un gato")
elif mascota =='perro':
    print("tienes un perro")
else:
    print("No se que animal tienes")
    
edad = 16
calificacion = 9

if edad < 18:
    print("eres menor de edad")
    if calificacion >= 7:
        print("Aprobaste")
    else:
        print("Reprobaste")
else:
    print("Eres adulto")