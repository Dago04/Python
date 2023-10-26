from pathlib import *

#base = Path.home() #ruta absoluta del usuario del pc

#guia = Path(base,"Europa","España",Path("Barcelona","Sagrada_Familia.txt"))
#guia2 = guia.with_name("La_Pedrera.txt")
#print(guia.parent.parent)


guia = Path(Path.home(),"Europa")

#itera cada txt del directorio europa
for txt in Path(guia).glob("**/*.txt"): #.glob("*.txt") jala todos los txt del directorio actual pero  
    #.glob("**/*.txt" jala todos los directorios relacionados al directorio actual
    print(txt)
    
    
    
guia2 = Path("Europa","España","Barcelona","Sagrada Familia.txt")
en_europa = guia2.relative_to(Path("Europa"))
en_espania = guia2.relative_to(Path("Europa","España"))

print(en_europa)
print(en_espania)


