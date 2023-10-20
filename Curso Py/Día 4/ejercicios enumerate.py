#lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

#for i,nombres in enumerate(lista_nombres):
  
    #print(f"Nombre {nombres} se encuentra en el indice {i+1}")
    
    


lista_indices = list(enumerate("Python"))

print(lista_indices)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombres in enumerate(lista_nombres):
    if nombres.startswith('M'):
        print(indice,nombres)
    else:
       continue
  
