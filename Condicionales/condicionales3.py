#Cree un codigo donde simule una calculadora y con la inicial del nombre de cada operador realice la funcion que desee.

numero1=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese otro numero: "))
numero3=int(input("Ingrese un tercer numero: "))

operacion = input("Ingrese la operacion que desea realizar:").upper()

if operacion=="S":
        suma = numero1+numero2+numero3
        print(f" La suma de los numeros es: {suma}")
elif operacion=="R":
     resta = numero1-numero2-numero3
     print(f"La resta de los numeros es: {resta}")
elif operacion=="M":
     multiplicacion= numero1*numero2*numero3
     print(f"La multiplicacion de los numeros es: {multiplicacion}")
elif operacion=="D":
     division= numero1/numero2/numero3
     print(f"La division de los numeros es: {division}")

else:
    print("La operacion no esta en las opciones.")
    print("Vuelve a ingresar una operacion matematica.")
    
    
    
    
    


