# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números
def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero."
    else:
        return a / b

# Función principal
def main():
    while True:
        print("Opciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Elija una opción (1/2/3/4/5): ")
        
        if opcion == '5':
            print("Saliendo de la calculadora.")
            break
        
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        if opcion == '1':
            print("Resultado: ", sumar(num1, num2))
        elif opcion == '2':
            print("Resultado: ", restar(num1, num2))
        elif opcion == '3':
            print("Resultado: ", multiplicar(num1, num2))
        elif opcion == '4':
            print("Resultado: ", dividir(num1, num2))
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
