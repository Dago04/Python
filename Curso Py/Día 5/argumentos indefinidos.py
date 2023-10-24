def suma(*args):
    total = 0
    
    for arg in args:
        total += arg
    return total


def suma_cuadrados(*args):
    total = 0
    
    for arg in args:
        total += arg**2
        
    return total


def suma_absolutos(*args):
    total =0 
    for arg in args:
        total+= abs(arg)
        
    return total


def numeros_persona(nombre, *args):
    suma = sum(args)
    
    return print(f"{nombre}, la suma de tus números es {suma}")


def prueba(num1,num2, *args, **kwargs):
   print(f"El primer valor es {num1}")
   print(f"El segundo valor es {num2}")
   
   for arg in args:
       print(f"arg = {arg}")
    
   for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        
    
args =[100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}
prueba(10,50,*args,**kwargs)

def cantidad_atributos(**kwargs):
   return len(kwargs)


def lista_atributos(**kwargs):
  
    return list(kwargs.items())


def describir_persona(nombre,**kwargs):
    print(f"Caracteristicas de {nombre}")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
        

describir_persona("María", color_ojos="azules", color_pelo="rubio")
