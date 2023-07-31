def crear_diccionario_colores():
    diccionario = {
        "rojo": "red",
        "blanco": "white",
        "verde": "green", 
        "negro": "black",
        "rosado": "pink",
        "amarillo": "yellow",
        "naranja": "orange",
        "purpura": "purple",
        "azul": "blue",
        "lila": "lilac"
    }
    return diccionario

colores = ['rojo', 'blanco', 'verde', 'negro', 'rosado', 'amarillo', 'naranja', 'purpura', 'azul', 'lila', 'marron']

diccionario = crear_diccionario_colores()

for color in colores:
    if color in diccionario:
        print(color, "->", diccionario[color])
    else:
        print(color, "no está en el diccionario")

# Modificar el nombre del color "rojo" a "morado"
diccionario["rojo"] = "morado"
print(diccionario)
