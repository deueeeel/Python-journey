# Escribir en un archivo
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("Primera nota\n")
    f.write("Segunda nota\n")

# Leer un archivo
with open("notas.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)

# Agregar al archivo (append)
with open("notas.txt", "a", encoding="utf-8") as f:
    f.write("Tercera nota\n")

# Leer después del append
with open("notas.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)

import json

contacto = {
    "nombre": "Deuel",
    "email": "deuel@email.com",
    "telefono": "0991234567"
}

# Guardar en JSON
with open("contacto.json", "w") as f:
    json.dump(contacto, f, indent=4)

# Leer el JSON
with open("contacto.json", "r") as f:
    recuperado = json.load(f)
    print(recuperado["nombre"])
    print(recuperado["email"])