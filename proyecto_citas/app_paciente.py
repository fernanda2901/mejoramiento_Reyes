from paciente import Paciente   # importamos los modulos y clases 
from medico import Medico
from citas_medicas import CitaMedica
from Menu_pasiente import mostrar_menu
from basedatos import cargar_citas, guardar_citas

if __name__ == "_main_": # se crea instancias de medico y paciente 
    medico2 = Medico("Dr. juan manuel", "Consultorio b", "miercoles y viernes de 8:00 AM - 5:00 PM")
    paciente2 = Paciente("diego", "medico general" )
    paciente2.citas = cargar_citas() # Carga de citas médicas del paciente desde la base de datos

    while True:    #generamos el bucle infinito para mostrar menu
        mostrar_menu()
        opcion = int(input("Ingrese el número de opción que desea realizar: "))

        if opcion == 1: # registra una nueva cita medica 
            fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
            hora = input("Ingrese la hora de la cita (HH:MM AM/PM): ")
            motivo = input("Ingrese el motivo de la cita: ")
            especialista = input("Ingrese la especialidad del médico que necesita: ")
            cita_nueva = CitaMedica(paciente2, medico2, fecha, hora, motivo) # se crea una instacia citamedica con los atributos proporcionados
            medico2.especialidad = especialista # actualiza la especialidad del medico 
            paciente2.registrar_cita(cita_nueva) # registra la nueva cita en el paciente 
           

            print("¡Cita médica registrada exitosamente!")

        elif opcion == 2: # consultamos las citas medicas registradas
            citas_registradas = paciente2.consultar_citas_registradas()
            if citas_registradas:
                print("Citas médicas registradas:")
                for cita in citas_registradas:
                    print(cita.obtenerInformacionCita())
            else:
                print("No tiene citas médicas registradas.")

        elif opcion == 3: # consultar las citas medicas agendadas del medico
            citas_agendadas = medico2.consultar_Citas_Agendadas()
            if citas_agendadas:
                print("Citas médicas agendadas:")
                for cita in citas_agendadas:
                    print(cita.obtenerInformacionCita())
            else:
                print("No tiene citas médicas agendadas.")

        elif opcion == 4: # eliminar una citas medica registrada del paciente 
            citas_registradas = paciente2.consultar_citas_registradas()
            if citas_registradas:
                print("Citas médicas registradas:")
                for idx, cita in enumerate(citas_registradas): #idx se utiliza como contador para enumerar las citas medicas 
                    print(f"{idx + 1}. {cita.obtenerInformacionCita()}")

                num_cita_eliminar = int(input("Ingrese el número de la cita que desea eliminar: "))
                if num_cita_eliminar > 0 and num_cita_eliminar <= len(citas_registradas):
                    cita_eliminar = citas_registradas[num_cita_eliminar - 1]
                    paciente2.eliminar_cita_propia(cita_eliminar)
                    print("¡Cita médica eliminada exitosamente!")
                else:
                    print("Opción inválida.")
            else:
                print("No tiene citas médicas registradas.")

        elif opcion == 5: #guardar las citas medicas en la base de datos y salir del programa 
            guardar_citas(paciente2.citas)
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.")