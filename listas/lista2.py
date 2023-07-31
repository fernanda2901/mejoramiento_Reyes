 #Llenar un arreglo de n elementos con numeros generados con la funcion aleatoria. No puede haber números repetidos.
 #Si intenta ingresar al arreglo un número que ya existe, imprimirlo para anunciar que ese número ya está en el arreglo.

import random #nos permite generar números aleatorios

def llenar_arreglo(n): #Definimos la función, que recibe como parámetro el tamaño n del arreglo que deseamos llenar con números aleatorios
    if n <= 0: #se verifica si el valor de n es menor o igual a cero
        print("El tamaño del arreglo debe ser mayor que cero.")
        return [] #la funcion devuelve una lista vacia
        
    arreglo = set() #Creamos un conjunto llamado arreglo
    #es una estructura de datos que no permite elementos repetidos

    while len(arreglo) < n: #generar números aleatorios hasta que el tamaño del conjunto arregloalcance 
        numero = random.randint(1, 100)  # Números aleatorios entre 1 y 100
        if numero not in arreglo: # si el número generado ( numero) no está presente en el conjunto arreglo
           #si no esta presente
            arreglo.add(numero) # se agrega al conjunto
        else:
            print(f"El número {numero} ya está en el arreglo.")

    return list(arreglo)

def main():
    try:
        n = int(input("Ingrese el tamaño del arreglo: "))
        arreglo_resultado = llenar_arreglo(n)#Llamamos a la función llenar_arreglo(n)para obtener el arreglo resultante sin números repetidos.
        print("Arreglo generado:", arreglo_resultado)
    except ValueError:
        print("Error: Ingrese un número entero válido.")

main()




