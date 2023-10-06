nombre = input("Digite el nombre del empleado ")
ventas = input("Digite el total de ventas realizadas por el empleado ")
ventas = int(ventas)

comision = ventas * 0.13 
comision = round(comision)

print(f"nombre {nombre} \nventas {ventas} \nPorcentaje de comision : {comision}")