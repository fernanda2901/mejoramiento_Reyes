""" Cree un codigo que le permita calcular cuantas horas trabaja en un mes y cuanto se gana al mes ingresando su pago diario al dia 
"""

horas_diarias=int(input("Ingrese las horas trabajadas por el dia: "))
dias_trabajados=int(input("Ingrese cuantos dias trabajo: "))
pago_diario=float(input("Ingrese su salario por dia: "))

if horas_diarias > 0 and pago_diario > 0 and dias_trabajados >0:
    horas_trabajadas= horas_diarias * dias_trabajados
    salario_mensual= horas_trabajadas* pago_diario

    print("Las horas trabajadas al mes fueron:", horas_trabajadas )

    print("Salario mensual:", salario_mensual)

else:
    print("Ese valor fue invalido, Ingrese un valor nuevo. ")
    