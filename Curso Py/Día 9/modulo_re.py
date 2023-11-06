import re

# texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'

'''patron = 'ayuda'

busqueda = re.findall(patron, texto)


for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())
'''
'''texto = 'llama al 564-525-6588 ya mismo'

# re.compile() sirve para agrupar el patron y de esta manera poder buscar los items del patron con la función group()
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado = re.search(patron, texto)
# resultado.group() ese metodo lo que hace es mostrarnos el patron a buscar
print(resultado.group(1))
'''

'''clave = input("Clave: ")

patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)

print(chequear)'''

texto = 'No atendemos los lunes por la tarde'

# buscar = re.search(r'lunes|martes', texto)
#   buscar = re.search(r'....demos...', texto)
# ^ buscar primera letra, $ buscar ultima letra
buscar = re.findall(r'[^\s]+', texto)
print(' '.join(buscar))
print(buscar)
