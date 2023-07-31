#Determinar si un número es o no es perfecto. Un numero es 
#perfecto si la suma de sus divisores sin incluir el propio número es igual a este 

def perfecto(): #defenimos la funcion sin ningun paramentro
    numero_perfecto = int(input("Ingresa un numero: "))
    calcular_perfecto = 1 #recorre todos los numeros desde uno
    suma = 0 #se usa para almacenar la suma de los divisores encontrados

    # Recorre todos los números desde 1 hasta (numero_perfecto - 1)
    while calcular_perfecto < numero_perfecto: #entra en el bucle hasta verificar que, calcular_perfecto sea menor que numero_perfecto
        if numero_perfecto % calcular_perfecto == 0: #si el nuemro perfecto es divisible por calcular perfecto y el resultado es cero
                                                    #entonces calcular perfeco es divisor de numero perfecto
            suma += calcular_perfecto                # se le agrega a la variable suma

        calcular_perfecto += 1 #se incremeta en uno para pasar alnum y buscar mas divisores

    if suma == numero_perfecto : #si la suma delos divisores es igual a  numeroperfecto
        print("El numero es perfecto.")
    else:
        print("El numero no es perfecto :(")

perfecto()