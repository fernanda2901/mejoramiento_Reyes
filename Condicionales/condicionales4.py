#Solicite la hora en formato horas, minutos y segundos. Imprima en pantalla la hora que será dentro de 1 segundo

def calcular_hora():

    hora= int(input("Ingrese la hora: "))
    minuto= int(input("Ingrese los minutos: "))
    segundo= int(input("Ingrese los segundos: "))

    segundo= int(segundo + 1) #Se incrementa el valor de segundo en 1 para calcular la hora después de un segundo adicional

    minuto=int(((minuto * 60) + segundo) / 60) #Se calcula el total de minutos teniendo en cuenta los segundos adicionales
                                               #sumando los minutos actuales convertidos a segundos 
                                               #se divide entre 60 para tener los minutos
 
    if segundo== 60: #  si segundo es igual a 60
        tiempoSegundos= int(0) #se crea tiempoSegundos en 0, para que el segundo adicional lleve a cabo un nuevo minuto.
    else:
        tiempoSegundos = int(segundo)

    if minuto== 60:  # Si minuto es igual a 60
        tiempoMinuto= int(0) # en 0, para que el minuto adicional lleve una nueva hora.
    else: 
       tiempoMinuto = int(minuto)

    tiempoHoras = int(((hora * 60) + minuto ) / 60) #Se calcula el total de horas teniendo en cuenta los minutos adicionales
                                                    # sumando las horas actuales convertidas a minutos y el valor de minuto
                                                    #se divide entre 60 para tener las horas finales.
                                                

    if(tiempoHoras == 24): #si tiempoHoras es igual a 24 horas
        tiempoHoras = int(0) # se pone en 0, ya que el segundo adicional llevaría a cabo un nuevo día.

    print("El tiempo dentro de un segundo es:"+str(tiempoHoras)+":"+str(tiempoMinuto)+":"+str(tiempoSegundos))    
       
calcular_hora()