monedas = 5

while monedas >0: 
    print(f"Tengo {monedas} monedas")
    monedas = monedas-1
    
    if monedas == 0:
        print("Se acabaron las monedas")
        
        

respuesta ='s'

while respuesta == 's':
    respuesta = input("quieres seguir? (s/n)")
else:
    print("Saliendo")
    


while respuesta =='s':
    pass


nombre = input("Tu nombre: ")

for letra in nombre:
    if letra=='d':
        break #continue
    print(letra)
