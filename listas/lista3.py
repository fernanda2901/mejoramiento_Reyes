"""Llenar un arreglo de n elementos con números generados con la función random. N es 
ingresado por el usuario
a. Imprimir arreglo original (El primero que se generó) 
b. Suma 
c. Promedio 
d. Mayor 
e. Menor 
f. Ordenar ascendente (No perder el arreglo original; el del punto a) 
g. Ordenar descendente (No perder el arreglo original; el del punto a) 
j. Buscar. Decir si encuentra el número, en qué posición(es) está, cuantas veces está"""


import random #permite generar números aleatorios

def calcular_lista(): #Se define la función sin ningún parámetro.


    n = int(input("Ingrese el tamaño de la lista:"))
    lista = [] #Se crea una lista vacia
    for i in range(n):
        lista.append(random.randint(1, 100)) # en cada iteración se agrega un número aleatorio entre 1 y 100 
    print("La lista original es:", lista)

    suma = sum(lista) #Se calcula la suma de todos los elementos
    print("La suma de la lista es:", suma)
    
    promedio = suma / n #Se calcula el promedio de la lista dividiendo la suma por el tamaño de la lista
    print("El promedio de la lista es:", promedio)
    
    mayor=max(lista) #Se encuentra el numero mayor de la lista utilizando max
    print("El numero mayor de la lista es", mayor)

    menor = min(lista) #Se encuentra el número menor de la lista utilizando min
    print("El número menor de la lista es:", menor)

    ascendente = sorted(lista) #Se ordena la lista de manera ascendente utilizando sorted
    print("Lista ordenada de manera ascendente:", ascendente)

    descendente = sorted(lista, reverse=True)
    print("Lista ordenada de una forma descendente:", descendente)

    numero = int(input("Ingrese el número que desea buscar en la lista:"))
    if numero in lista:
        posicion = lista.index(numero) #se utiliza para obtener la primera posición (índice) en la que aparece el elemento numero dentro de la lista
        print("El número", numero, "se encuentra en la posición", posicion, "de la lista.")
    else:
        print("El número", numero, "no se encuentra en la lista.")

calcular_lista()