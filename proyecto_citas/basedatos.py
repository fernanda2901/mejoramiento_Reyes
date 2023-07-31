from paciente import Paciente
from medico import Medico
from citas_medicas import CitaMedica

def guardar_citas(citas):  # esta funcion se encarga de guardar las citas en un archivo de texto
    with open('citas.txt', 'w') as file:
        for cita in citas:  #Escribir los datos de la cita separados por | en una línea del archivo
            file.write(f"{cita.paciente.nombre}|{cita.medico.nombre}|{cita.medico.especialidad}|{cita.fecha}|{cita.hora}|{cita.motivo}\n")

def cargar_citas(): # esta funcion se encarga de cargar citas medicas desde un archivo de texto
    try:
        with open('citas.txt', 'r') as file:
            lineas = file.readlines()
            citas = []
            for linea in lineas:
                datos = linea.strip().split('|')
                 # Crear instancias de Paciente, Medico y CitaMedica a partir de los datos en la línea
                paciente = Paciente(datos[0], datos[1])
                medico = Medico(datos[2], datos[3], datos[4]) 
                cita = CitaMedica(paciente, medico, datos[5], datos[6], datos[7])
                citas.append(cita)
            return citas
    except FileNotFoundError:
        return []