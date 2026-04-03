# Bucle for con range()
print("Tabla del 9:")
for a in range(1, 11):
    print(f"9 x {a} = {9 *a}")
#cambié la i por la a; detalle estético nomás 

# Bucle while — cuenta regresiva
contador = int(input("Dime un número entre el 10 y el 20: "))
#agregué un input :)
while contador > 0:
    print(f"⏱ {contador}")
    contador -= 1
print("¡Despegue aaaaa! 🚀")
#agregué un "aaaa" para más diversión

# break y continue
for num in range(1, 40):
    if num % 3 == 0:
        continue           # salta divisibles para 3
    if num > 10:
        break              # para al llegar a 11
    print(num)             # imprime impares del 1 al 9