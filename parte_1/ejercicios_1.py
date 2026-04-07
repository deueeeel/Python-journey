#Tarjeta de presentación
#Crea variables con tu nombre, edad, ciudad y hobby favorito. 
#Imprímelos con un f-string formateado como una tarjeta.

neim = input("Nombre: ")
age = input("Edad: ")
city = input("Ciudad: ")
hobby = input("Hobby favorito: ")

print(f"Un gusto en conocerte {neim} es bueno tener a alguien de {age} años que seas de {city} y que tu hobby favorito sea {hobby}")

#Calculadora básica
#Pide dos números al usuario con input(), conviértelos a 
#float con float(), y muestra suma, resta, multiplicación y división.
number_1 = input("Número 1: ")
number_2 = input("Número 2: ")

suma = float(number_1) + float(number_2) 
resta = float(number_1) - float(number_2) 
multiplicación = float(number_1) * float(number_2) 
división = float(number_1) / float(number_2) 
print(suma)
print(resta)
print(multiplicación)
print(división)

#Conversor de temperatura
#Pide una temperatura en Celsius, conviértela a Fahrenheit (F = C × 9/5 + 32) 
# y muestra el resultado formateado.

temperatura = int(input("Cuál es la temperatura? "))
fahrenheit = (temperatura * 9/5 + 32)
print(f"{temperatura}°C es {fahrenheit} en °F")