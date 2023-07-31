#Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig manera:
#Si trabaja 40 horas o menos se le paga $2600 por hora
#Si trabaja más de 40 horas se le paga $2600 por cada una de las primeras 40
#horas y $5000 por cada hora extra

def calcular_salario(pago=0): #se define la funcion salario sin parametros

 hora_trabajada= int(input("Ingrese las horas trabajadas: ")) # creamos un variable con la funcion int para numeros enteros 
    
 if hora_trabajada > 40:
        horas_extras= hora_trabajada - 40 #se calcula las horas extras, horas extras es igual a horas trabajadas menos las primeras 40horas
        pago=(40 * 2600) + (horas_extras * 5000) #se calcula el pago multiplicando las primeras 40horas por el pago 
                          #a ese resultado se le suma las horas extras multiplicado por 5000 que eso valen
 else:
  pago=hora_trabajada * 2600 #se calcula el pago sin horas extras que es igual a las horas trabajdas por 2600
  print(f"Su pago semanal por {hora_trabajada} horas es ${pago}")

 if pago==0:
   calcular_salario(pago)
   
calcular_salario() #llamamos la funcion para realizar el calculo
