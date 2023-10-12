##diccionario = {'c1':'valor1', 'c2':'valor2'}
#print(diccionario)


#resultado = diccionario['c1']

#print(resultado)

#cliente ={'nombre':'Juan','apellido':'Fuentes','peso':88,'talla':1.80}
#consulta = cliente['apellido']
#print(consulta)

#dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}

#print(dic['c2'][1])

#print(dic['c3']['s2'])

#dic = {'c1':['a','b','c'], 'c2':['d','e','f']}

#E = dic['c2'][1].upper()
#print(E)

dic ={1:'a', 2:'b'}
print(dic)

dic[3] = 'c'
print(dic)



print(dic.keys())

print(dic.values())

print(dic.items())


#Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.

#Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa 
# misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])


#Práctica Diccionarios 3
#Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:

#nombre: Karen

#apellido: Jurgens

#edad: 36

#ocupacion: Editora

#pais: Colombia

#para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}


mi_dic["edad"] = 36 
mi_dic["ocupacion"] = "Editora"
mi_dic['pais'] = "Colombia"

print(mi_dic)