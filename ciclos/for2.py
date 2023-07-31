#Determinar los divisores de un  número introducido por teclado 
def divisores():
    try:
        numero = int(input("Ingrese un número positivo: "))
        
        if numero <= 0:
            print("El número debe ser positivo y mayor que cero.")
            return

        divisores_encontrados = [] #Se inicializa una lista para guardar los divisores del número

        for i in range(1, numero + 1): # iterar desde 1 hasta numero + 1
    
            if numero % i == 0: #si el número es divisible por i es un divisor del número
                divisores_encontrados.append(i) # y se agrega a la lista

        if len(divisores_encontrados) == 2: # se verifica el tamaño de la lista
                                             #esto significa que el número tiene solo dos divisores: 1 y el propio número
                                             
            print(f"{numero} es un número primo.")
        else:
            print(f"Los divisores de {numero} son: {divisores_encontrados}")

    except ValueError:
        print("Error: Solo se permiten números enteros.")

divisores()
