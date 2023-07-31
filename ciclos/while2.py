#¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000? 

def numero_primo(num): #se crea una funcion con el parametro num
    if num < 2: #si el num es menor de dos retorna un false/  # pq los números primos son mayores o iguales a 2
        return False 
    
    i = 2 #se inicia la variable i para comenzar a mirar que "num" inicie desde 2.

    while i < num: #mientras i sea menor que el numero
        if num % i == 0: #si num es divisible por i y eso es igual a 0
                        #significa que  num no es primo
            return False #retorna y falso 
        i += 1# si no se encuentra ningún divisor, significa que "num" es un número primo devuelve "True".
    return True

primos = []  # Lista para almacenar los números primos encontrados

for num in range(1, 1001): #que registra todos los números desde 1 hasta 1000 
    if numero_primo(num): #se llama la funcion para verificar si num es primo o no
        primos.append(num) #Si es primo, se agrega a la lista "primos" 

cantidad_primos = len(primos) #se calcula la variable para la logitud de la lista primos

print("Números primos comprendidos entre 1 y 1000:")
print(primos)
print("Cantidad de números primos:", cantidad_primos)