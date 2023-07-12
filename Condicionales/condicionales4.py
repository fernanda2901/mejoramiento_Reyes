#Crea un codigo que ingrese una vocal y diga si es vocal o no 

vocal= input("Ingrese una vocal:").lower()

if vocal=="a" or vocal=="e" or vocal=="i" or vocal=="o" or vocal=="u":
    print("El caracter es correcto")
    print("Es una vocal")

else:
    print("El caracter es erroneo")
    print("No es una vocal")