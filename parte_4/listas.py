# Listas: colección ordenada y mutable
fruits = ["apple", "banana", "naranja", "sandía"]
nums = [1, 2, 3, 4, 5]

print(fruits[0])       # manzana (primer elemento)
print(nums[-1])      # naranja (último elemento)

fruits.append("uvas")     # agrega al final
fruits.insert(1, "kiwi") # inserta en posición 1
fruits.remove("banana")  # elimina por valor

print(fruits)

# Recorrer lista
for fruit in fruits:
    print(f"🍎 {fruit}")

#Recorrer lista pero con capitales de países

capitals = ["Quito", "Vienna", "Madrid", "Mexico City", "Tokyo"]
for capital in capitals:
    print(f"🏙️ {capital}")

# List comprehension — forma compacta y pythonica
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]

pares = [x for x in nums if x % 2 == 0]
print(pares)       # [2, 4]
