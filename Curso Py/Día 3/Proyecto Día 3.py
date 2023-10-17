
texto = input("Ingrese un texto : ")

letras = []

texto = texto.lower()

letras.append(input("Digite la primera letra ").lower())
letras.append(input("Digite la segunnda letra ").lower())
letras.append(input("Digite la tercera letra ").lower())

print("\n")
print("Cantidad de letras")

cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"La letra '{letras[0]}' se repite {cantidad_letras1} veces")
print(f"La letra '{letras[1]}' se repite {cantidad_letras2} veces")
print(f"La letra '{letras[2]}' se repite {cantidad_letras3} veces")

print("\n")
print("Cantidad de palabras")

listaTexto= texto.split()

print(f"Hemos encontrado {len(listaTexto)} palabras en tu texto")

print("\n")
print("Primera y Ultima Palabra del texto")

primera_palabra = texto[0]
ultima_palabra = texto[-1]


print(f"La primera palabra de tu texto es {primera_palabra}")
print(f"La ultima palabra de tu texto es {ultima_palabra}")


print("\n")
print("texto invertido")

listaTexto.reverse()
texto_inverso = ' '.join(listaTexto)

print(f"Si ordenamos tu texto al revez va decir : {texto_inverso}")


print("\n")
print("buscando palabra python")
buscar_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palaba 'python' {dic[buscar_python]} se encuentra en el texto")