# Calculadora con Funciones
#Refactoriza la calculadora del Proyecto 1 usando funciones: sumar(), restar(), multiplicar(), 
#dividir(), mostrar_menu().
#El programa principal solo llama funciones. Añade manejo de división por cero con if.


def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir para 0"
    return a / b

def mostrar_menu():
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


# Programa principal
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Adiós 👋")
        break

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", sumar(a, b))
    elif opcion == "2":
        print("Resultado:", restar(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicar(a, b))
    elif opcion == "4":
        print("Resultado:", dividir(a, b))
    else:
        print("Opción inválida")