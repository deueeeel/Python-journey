#Crea un programa con un menú de restaurante. Muestra opciones numeradas, 
# el usuario elige con input(), calcula el total, 
# pregunta si quiere pedir algo más (while loop), 
# y al final muestra el ticket con todos los pedidos. 
# Usa if/elif para validar la selección.

menu = "El menú que tenemos es: pizza, sushi, chicken wings, pho"
print(menu)
print("Precios: pizza 4.50, sushi 8.99, chicken wings 12.99, encebollado 2.99")

total_general = 0

while True:
    item = input("¿Qué vas a comprar? ")

    if item == "pizza":
        precio = 4.50
    elif item == "sushi":
        precio = 8.99
    elif item == "chicken wings":
        precio = 12.99
    elif item == "encebollado":
        precio = 2.99
    else:
        print("Producto no válido")
        continue

    cantidad = int(input("¿Cuánto vas a comprar? "))
    total = cantidad * precio
    total_general += total

    algo_mas = input("¿Quieres pedir algo más? (s/n): ")
    if algo_mas != "s":
        break

iva = total_general * 0.16
total_final = total_general + iva
print(f"El total por tu compra será de {total_final:.2f}")
print("Gracias por tu compra!! :)")