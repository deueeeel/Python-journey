#Esto son funciones!
def hola():
    print("Hola te saludo desde una función")
hola()
# Feliz cumpleaños
def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print("Feliz cumpleaños a ti!")
    print(f"Que cumplas feliz tus {age} años!")
    print("Hasta el año 3000!")

happy_birthday("Deuel", 22)
happy_birthday("Paco", 21)
happy_birthday("Pedro", 24)

#Funcion de nombre completo
def nombre_completo(nombre, apellido):
    name = nombre.capitalize()
    apellido = apellido.capitalize()
    return nombre + " " + apellido
nombre_completo_1 =nombre_completo ("Paco", "López")

print(nombre_completo_1)
