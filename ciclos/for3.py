# Determinar si un numero es o no es primo 

def numero_primo(num): # se define la funcion, que toma un argumento(num) el que sera el numero a verificar
     
    if num < 2:    #  si el numero es manor que 2, ya que los numeros primos son mayores o iguales a 2
        return False     # si enumero es menor que dos se retorna false
    
    for i in range(2,num): #entramos en un bucle 'for' que itera desde 2 hasta 'num - 1'.
       
        if num % i == 0:   # se verifica si el número 'num' es divisible por 'i', es decir, si el resto de 'num' dividido por 'i' es igual a 0.
            return False   # Si el número es divisible por algún valor de 'i', entonces no es primo y retornamos 'False'.
    
    return True # # Si el bucle completa todas las iteraciones sin encontrar un divisor, entonces 'num' es primo y retornamos 'True'.
    
numero= int(input("ingrese un numero: "))

if numero_primo(numero): ## Llamamos a la función 'numero_primo(numero)' para determinar si el número ingresado es primo o no.
    
    print(f"{numero} es un numero primo. ")
else:
    print(f"{numero} no es un numero primo. ")