def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion


@decorar_saludo
def mayusculas(texto):
    print(texto.upper())


def minisculas(texto):
    print(texto.lower())


mayuscula_dec = decorar_saludo(mayusculas)
