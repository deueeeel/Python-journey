# Diccionarios: pares clave-valor
persona = {
    "name": "Paco",
    "age": 21,
    "city": "Guayaquil",
    "estudiante": True
}

print(persona["name"])          # Paco
print(persona.get("email", "N/A")) # N/A (no lanza error)
print(f"Es estudiante? {persona['estudiante']}") #Imprime si es o no estudiante

# Agregar y modificar
persona["email"] = "paco@email.com"
persona["age"] = 25

# Recorrer el diccionario
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

# Lista de diccionarios — base de datos simple
estudiantes = [
    {"nombre": "Luisao", "nota": 95},
    {"nombre": "Pedro", "nota": 82},
    {"nombre": "Marcos", "nota": 78},
    {"nombre": "Alejandro", "nota": 84},
]

for est in estudiantes:
    print(f"{est['nombre']}: {est['nota']}/100")