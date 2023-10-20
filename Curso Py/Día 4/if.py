#num1 = int(input("Ingresa un número:"))
#num2 = int(input("Ingresa otro número:"))


#if num1 > num2:
    #print(f"El numero {num1} es mayor que {num2}")
#elif num2>num1:
    #print(f"El número {num2} es mayor que {num1}")
#else:
    #print(f"El número {num1} es igual que el número {num2}")



edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad >= 18 and not tiene_licencia:
    print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
    
    

sabe_python = False
habla_ingles = True

if sabe_python and habla_ingles:
    print("Cumples con los requisitos para postularte")
elif sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")