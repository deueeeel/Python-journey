# Funciones matemáticas
# Crea funciones: area_rectangulo(base, alto), 
# area_circulo(radio), volumen_esfera(radio). 
# Pide valores al usuario y muestra resultados.

import math

def area_rectangulo(base, alto):
    return base * alto

def area_circulo(radio):
    return math.pi * (radio ** 2)

def volumen_esfera(radio):
    return (4/3) * math.pi * (radio ** 3)

# Pedir datos
base = float(input("Ingresa la base del rectángulo: "))
alto = float(input("Ingresa el alto del rectángulo: "))

radio = float(input("Ingresa el radio: "))

# Resultados
print(f"Área del rectángulo: {area_rectangulo(base, alto):.2f}")
print(f"Área del círculo: {area_circulo(radio):.2f}")
print(f"Volumen de la esfera: {volumen_esfera(radio):.2f}")

#Validador de datos
#Función es_email_valido(email) que verifica si tiene @ y un punto después. 
#Función es_contraseña_segura(pwd) que verifica mínimo 8 caracteres

def es_email_valido(email):
    if "@" in email:
        partes = email.split("@")
        if "." in partes[1]:
            return True
    return False


def es_contraseña_segura(contraseña):
    if len(contraseña) >= 8:
        return True
    else:
        return False


# Pruebas de email y contraseña
email = input("Ingresa tu email: ")
if es_email_valido(email):
    print("Es un correo válido")
else:
    print("No es un correo válido")


pwd = input("Ingresa tu contraseña: ")
if es_contraseña_segura(pwd):
    print("Es una contraseña segura")
else:
    print("No es una contraseña segura")