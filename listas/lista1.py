#llenar dos arreglos con la funcion ramdon compararlos y decir cual de las dos listas tiene el numero mayor
#de igual forma con el numero mayor calcular cual de los dos tienen mayor cantidad de pares

import random

def generar_lista_aleatoria(n, min_val, max_val):
    # Genera una lista aleatoria de tamaño n con elementos entre min_val y max_val (ambos inclusive)
    return [random.randint(min_val, max_val) for _ in range(n)]

def contar_pares(lista):
    # Cuenta la cantidad de números pares en la lista
    return sum(1 for num in lista if num % 2 == 0)

def comparar_listas(lista1, lista2):
    # Encuentra el número mayor en cada lista y los compara
    max_lista1 = max(lista1)
    max_lista2 = max(lista2)

    # Imprime el contenido de ambas listas
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)

    if max_lista1 == max_lista2:
        # Si ambos tienen el mismo número mayor, muestra el resultado
        print("Ambas listas tienen el mismo número mayor:", max_lista1)
    elif max_lista1 > max_lista2:
        # Si lista1 tiene el número mayor, muestra el resultado
        print("Lista 1 tiene el número mayor:", max_lista1)
    else:
        # Si lista2 tiene el número mayor, muestra el resultado
        print("Lista 2 tiene el número mayor:", max_lista2)

    # Cuenta la cantidad de números pares en cada lista
    pares_lista1 = contar_pares(lista1)
    pares_lista2 = contar_pares(lista2)

    if pares_lista1 == pares_lista2:
        # Si ambas listas tienen la misma cantidad de números pares, muestra el resultado
        print("Ambas listas tienen la misma cantidad de números pares:", pares_lista1)
    elif pares_lista1 > pares_lista2:
        # Si lista1 tiene mayor cantidad de números pares, muestra el resultado
        print("Lista 1 tiene mayor cantidad de números pares:", pares_lista1)
    else:
        # Si lista2 tiene mayor cantidad de números pares, muestra el resultado
        print("Lista 2 tiene mayor cantidad de números pares:", pares_lista2)

# Configuración
tamano_listas = 10
minimo_valor = 1
maximo_valor = 100

# Generar listas aleatorias
lista1 = generar_lista_aleatoria(tamano_listas, minimo_valor, maximo_valor)
lista2 = generar_lista_aleatoria(tamano_listas, minimo_valor, maximo_valor)

# Comparar listas
comparar_listas(lista1, lista2)