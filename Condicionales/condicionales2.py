"""hacer un menu que tenga cuatro opciones, que pueda digitar su numbre, su telefono su correo y su identificacion"""
nombre = 0
correo= 0
numero= 0
id= 0 
print("*****Menú*****")
print("1. ingrese su nombre: ")
print("2. ingrese su correo: ")
print("3. ingrese su numero: ")
print("4. ingrese su id: ")
print("5.salir")
opcion= int(input("dijita la opcion del menu: "))

if opcion==1:
    NunNom= input("Ingrese su nombre: ")
    nombre = NunNom
    print(f"El nombre guardado es: {NunNom}")

elif opcion==2:
    NumCorreo= input("Ingrese su correo: ")
    correo = NumCorreo
    print(f"Verifique su correo: {NumCorreo} ")

elif opcion==3:
    NumNum=int(input("Ingrese su numero celular: "))
    numero=numero+ NumNum
    print(f"Su numero registrado es: {NumNum}")

elif opcion==4:
    NumId=int(input("Ingrese su Id: "))
    id=id + NumId
    print(f"Su Id registrado es: {NumId}")

elif opcion==5:
    print("gracias por utilizar este programa.")
