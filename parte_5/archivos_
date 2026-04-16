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

# JSON — guardar y cargar estructuras de datos
import json
#haré cambios de nombres y agregaré otros 
datos = {"nombre": "Carlos", "edad": 25, "hobbies": ["ver peliculas", "correr"]
            "nombre": "Pedro", "edad": 25, "hobbies": ["ver peliculas", "correr"]}
with open("datos.json", "w") as f:
    json.dump(datos, f, indent=4)

with open("datos.json", "r") as f:
    recuperado = json.load(f)
    print(recuperado["nombre"])