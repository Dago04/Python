#Dado el salario bruto y cantidad de ventas de un empleado que trabaja
#en una empresa de venta de autos.Calcular el salario neto teniendo en
#cuenta varios factores En primer lugar, se debe restar un 10.6% del
#salario bruto para cubrir el seguro de salud y un 7% adicional por
#concepto de impuesto de renta . Además, en esta empresa se pagan
#regalías por cada venta que realiza el empleado, el porcentaje de las
#regalías es del 2% sobre las ventas.

salario_bruto = float(input("Digite su salario bruto "))
cantidad_ventas= float(input("Digite la cantidad de ventas que ha realizado "))

porcentaje_seguro = 0.106
impuesto_renta = 0.07
porcentaje_regalias = 0.02

seguro = salario_bruto * porcentaje_seguro
renta =  salario_bruto* impuesto_renta
regalias = cantidad_ventas * porcentaje_regalias

salario_neto = salario_bruto-seguro-renta + regalias 

print("El salario neto del empleado es: " + str(salario_neto) + "\nEl porcentaje de seguro es de: " + str(seguro) + "\nEl impuesto sobre la renta es: " + str(renta) + "\nEl porcentaje en regalías es de: " + str(regalias))
