#Escribe un programa que pida tres números y que escriba si son los tres son iguales, si hay dos iguales o si son los tres distintos
   
def numeros(): #se define lafuncion sin ningun parametro

 try:
     
     num1=int(input("Ingrese el primer numero: "))
     num2=int(input("Ingrese el segundo numero: "))
     num3=int(input("Ingrese el tercer numero: "))
           
     if num1==num2==num3:
        print("Los tres numeros son iguales.")

     elif num1 == num2 or num1 == num3 or num2 == num3:
       print("Dos numeros son iguales")

     #elif num1!= num2 or num1 != num3 or num2 != num3:
     else:
       print("Los tres números que ha escrito son distintos.")       
    
   

 except ValueError:
    print("ERROR, EL VALOR INGRESADO ES ERRONEO //ES UNA LETRA//")

numeros()
    