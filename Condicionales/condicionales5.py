#cree un codigo donde el usuario ingrese su edad, si es mayor de edad puede votar si es menor de edad no puede votar"

edad= int(input("Ingrese su edad:"))

if edad>0 and edad<100:
    if edad>18:
        print("Eres mayor de edad , puedes votar correctamente.")

    else:
        print("Eres menor de edad, no puedes votar.")
else:
    print("Edad erronea.")