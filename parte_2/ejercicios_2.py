#1) Adivina el número
numero_correcto = 50
adivinanza = int(input("Adivina el número: "))
while numero_correcto != adivinanza:
    print("That's not the number, try it again!")
    adivinanza = int(input("Adivina el número: "))
print(f"Yeah, that's the number we are looking for: {numero_correcto}")

#2) FizzBuzz
# Clásico de programación: imprime del 1 al 100. 
# Múltiplos de 3: "Fizz". Múltiplos de 5: "Buzz". 
# Múltiplos de ambos: "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) 

#3) Verificador de contraseña
# Pide contraseña en un bucle. Solo da 3 intentos. 
# Si es correcta: "Acceso concedido". 
# Si agota intentos: "Cuenta bloqueada".

real_password = 'hola_papu'
numeroDeIntentos = 3
for i in range(numeroDeIntentos):
    contraseña = input("Ingrese por favor su contraseña: ")
    if contraseña == real_password:
        print("Gracias, bienvenido")
        break
    print('Incorrecto.  Te quedan %d intentos restantes' % (numeroDeIntentos-i-1))
