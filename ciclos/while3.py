# Calcular el máximo de números positivos introducidos por teclado, sabiendo que metemos números hasta que 
#introduzcamos uno negativo. El negativo no cuenta.

def maximo_positivo(): #definimos la funcion sin parametros
    maximo=None #en la variable maximo se agregan los numeros positivos ingresados por el usuario y mantiene un valor maximo, no se asigna ningun valor por none, esto indica que aun no a encontrado ningun numero valido 

    while True:   # Bucle infinito, seguirá pidiendo números hasta que se ingrese uno negativo.
        try:
             numero=int(input("ingrese un numero positivo: "))
        
             if numero < 0: # si numero es menor a 0, esdecir num negativo
                 break      # se rompe el bucle para terminar la entrada de números.
        
             if maximo is None or numero > maximo:  # Si "maximo" es "None"
                 maximo = numero                    # Se actualiza maximo con el valor del número ingresado si es mayor.
                                                    #maximo siempre va acontener el numero mas grande
        except ValueError:
             print("error introducir un numero valido.") # error al escribir un valor entero

    return maximo    #se devuelve el valor maximo que se a encontrado  

resultado = maximo_positivo ()    # se llama la funcion y se guarda en la variable resultado                                        

if resultado is not None: # si el resultado es none, esto es para saber si se encontraron numeros positivos validos  
   
    print("el maximo de los numeros es:",resultado )

else:
    print("no se introdujo ningun numero positivo.")