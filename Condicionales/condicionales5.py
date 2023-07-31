#Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
#valor del medio es 11. No use operadores lógicos

def numero_medio(num1, num2, num3): #se define lafuncion y toma como parametros tres argumentos
    
    #encontrar el número menor y el número mayor entre los tres números ingresadoss
    menor = min(num1, num2, num3)
    mayor = max(num1, num2, num3)

    # Calculamos el número medio utilizando operadores de comparación
    medio = num1 + num2 + num3 - menor - mayor # da como resultado el número medio, y se almacena en la variable medio

    return medio 

try:
    # Pedimos al usuario que ingrese tres números
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    # Llamamos a la función para encontrar el número medio
    medio = numero_medio(num1, num2, num3)

    if num1 == num2 == num3:
        print("Los tres números son iguales.")
    else:
        print(f"El número medio es: {medio}")

except ValueError:
    print("Error: Por favor, ingrese solo números válidos.")
