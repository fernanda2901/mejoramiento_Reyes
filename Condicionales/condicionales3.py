"""En un juego de preguntas a las que se responde “Si” o “No” gana quien
responda correctamente las tres preguntas. Si se responde mal a cualquiera de
ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
1. Colon descubrió América?
2. La independencia de Colombia fue en el año 1810?
3. The Doors fue un grupo de rock Americano?
"""
def jugar_preguntas():
    num_preguntas = 3 #Se inicia la variable num_preguntascon el valor 3, lo que significa que habrá tres preguntas en total.
    aciertos = 0 #será utilizada para contar la cantidad de preguntas que el usuario respondió bien

    for i in range(1, num_preguntas + 1):
        print("Pregunta", i)

        if i == 1:
            pregunta = "¿Colón descubrió América?"
            respuesta = "si"
        elif i == 2:
            pregunta = "¿La independencia de Colombia fue en el año 1810?"  
            respuesta = "si"
        elif i == 3:
            pregunta = "¿The Doors fue un grupo de rock americano?"
            respuesta = "si"

        print(pregunta)
        respuesta_usuario = input("Tu respuesta: ").lower()#Lee la respuesta y la convierte a minúsculas 

        if respuesta_usuario == "si" or respuesta_usuario == "no": #Verifica si la respuesta del usuario es "si" o "no"
            if respuesta_usuario == respuesta:#Si la respuesta es corretca, compara con la respuesta esperada
                print("¡Respuesta correcta!")
                aciertos += 1 # aumenta el contador de aciertosen 1
            else:
                print("Respuesta incorrecta.")
        else:
            print("Respuesta inválida. Por favor, responde 'sí' o 'no.'")
        print()

    print("Juego terminado.")
    print("Has acertado", aciertos, "preguntas de", num_preguntas, "preguntas.")

jugar_preguntas()
    
    
    
    
    


