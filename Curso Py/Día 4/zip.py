nombres = ['Ana','Hugo','Valeria']
edades= [65,29,42]
ciudades =['Lima','España','Mexico']

combinados = list(zip(nombres,edades,ciudades))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")

print(combinados)