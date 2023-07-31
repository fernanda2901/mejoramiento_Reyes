#Solicitar al usuario un número de hasta 9 dígitos e 
#imprimirlo en orden contrario. Ej. digito 6754 imprimo 4576 

def invertir_numero(numero): #Se define la función recibe un parametro numero
    # Convertimos el número en una cadena y luego invertimos la cadena

    numero_str = str(numero)
    numero_invertido_str = numero_str[::-1] #se invierte la cadena utilizando el slicing
    # toma todos los elementos de la cadena, pero en orden inverso.

    # Convertimos la cadena invertida nuevamente en un número entero
    numero_invertido = int(numero_invertido_str)
    
    return numero_invertido #devuelve el número invertido

while True: #el ciclo se repetirá indefinidamente hasta que se alcance una condición de finalización
    try:
        numero = int(input("Ingrese un número entero de hasta 9 dígitos: "))
        if 0 <= numero < 10**9:  # Rango de 0 a 999,999,999 (9 dígitos)
            numero_invertido = invertir_numero(numero) # procede a invertir el número
            print(f"El número invertido es: {numero_invertido}")
            break
        else:
            print("Error: Por favor, ingrese un número dentro del rango especificado (hasta 9 dígitos).")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

