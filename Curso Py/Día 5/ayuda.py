#dic = {'clave1':1,'clave2':500}

#a=dic.popitem()

#print(a)
#print(dic)



#metodo lstrip()

texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

a =texto.lstrip(',:%_#')

print(a)


#metodo insert en una lista, recibe como parametro la posición donde se va insertar y el elemento que queremos agregar
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 

frutas.insert(3,'naranja')


print(frutas)

#isdisjoint() verifica si hay elementos en comun entre ambos objetos
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}


conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)