texto = "Este es el texto de dago"

#metodo upper para poner el string en mayuscula
resultado = texto.upper()
#poner en minisculo
resultado = texto.lower()
#tomar elementos y los separa, seperandolos por los espacios vacios
resultado = texto.split("t")
#buscar elementos, sino se encuentra el resultado es -1
resultado = texto.find("z")
#reemplazar los elementos 
resultado = texto.replace("dago","Diego")

print(resultado)

a ="Aprender"
b ="Python"
c ="Es genial"
#une los textos
e =" ".join([a,b,c])

print(e)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
parrafo = frase.replace("difícil", "fácil").replace("mala", "buena")
print(parrafo)