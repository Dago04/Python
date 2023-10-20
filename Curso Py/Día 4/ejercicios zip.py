capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]


combinado = list(zip(paises,capitales))

for pais, capital in combinado:
    print(f"La capital de {pais} es {capital}")
    break

marcas = ['Adidas','Nike']
productos = ['Tennis','Zapatos']

mi_zip = zip(productos,marcas)
print(mi_zip)

español = ['uno','dos','tres','cuatro','cinco']
portugues = ['um','dois','três','quatro','cinco']
ingles = ['one','two','three','four','five']


numeros = list(zip(español,portugues,ingles))
print(numeros)