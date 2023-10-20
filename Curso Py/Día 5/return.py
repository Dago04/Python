def multiplicar(numero1,numero2):
    return numero1*numero2


resultado =multiplicar(1.5,5)
print(resultado)



#Ejercicio 1
def potencia(num1,num2):
    return num1**num2
    

resultado = potencia(3,4)
print(resultado)

#ejercicio 2
dolares = 5
def usd_a_eur(numero):
    conversion = numero * 0.90
    return conversion


euros = usd_a_eur(dolares)
print(euros)


#ejercicio 3
palabra = "Python"

def invertir_palabra(texto):
    texto = texto[::-1]
    return texto.upper()
    

resultado = invertir_palabra(palabra)
print(resultado)