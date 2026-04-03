# if / elif / else — toma de decisiones
edad = int(input("¿Cuántos años tienes? "))

if edad < 12:
    print("Eres niño/a")
elif edad < 18:
    print("Eres adolescente")
elif edad < 65:
    print("Eres adulto/a")
else:
    print("Eres adulto/a mayor")

# Operadores lógicos
llueve = input("¿Llueve hoy? (True or False): ")
tengo_paraguas = input("¿Tienes paraguas? (True or False): ")
#he agregado inputs aquí aunque en el ejercicio original no iban :D

if llueve == "True" and tengo_paraguas == "False":
    print("¡Vas a mojarte!")
elif llueve and tengo_paraguas:
    print("Estás protegido")