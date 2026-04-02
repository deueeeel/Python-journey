#Factura Simple
#Crea un programa que pida el nombre del cliente, precio de 3 productos 
# y sus cantidades. 
# Calcula el subtotal, aplica 16% de IVA 
# y muestra una factura formateada con f-strings. 
# Usa lo que aprendiste sobre variables, operadores y print.

nombre = input("Hola cómo te llamas? ")
producto_1 = input("Qué vas a llevar? ")
precio_1 = float(input("Cuánto vale el primer producto? "))
producto_2 = input("Qué vas a llevar? ")
precio_2 = float(input("Cuánto vale el segundo producto? "))
producto_3 = input("Qué vas a llevar? ")
precio_3 = float(input("Cuánto vale el tercer producto? "))

suma_3 = precio_1 + precio_2 + precio_3
iva = suma_3 * 0.16
total = suma_3 + iva

print(f"Ok, {nombre} el valor total por los 3 productos es {total}")