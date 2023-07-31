#from usuario import Usuario
class Medico():
     # Constructor de la clase, se ejecuta al crear una instancia de Medico
    def _init_(self, nombre, consultorio, horario_disponible):
        self.nombre = nombre     # Nombre del médico (cadena)
        self.especialidad = None   # Especialidad del médico (cadena) - inicialmente vacío
        self.consultorio = consultorio   # Consultorio del médico (cadena)
        self.horario_disponible = horario_disponible  # Horario disponible del médico (cadena)
        self.citas_agendadas = []  # Lista de citas médicas agendadas con el médico

    def consultar_Citas_Agendadas(self,paciente): #consultar las citas agendadas con un paciente específico
          #Utiliza una comprensión de listas para filtrar las citas del paciente en la lista de citas agendadas
         citas_paciente = [cita for cita in self.citas_agendadas if cita.paciente == paciente]
         return citas_paciente

    def definirHorarioDisponible(self, horario): #definir el horario disponible del médico
        self.horario_disponible = horario

    def eliminarCita(self, cita): #eliminar una cita de las citas agendadas del médico
        if cita in self.citas_agendadas:
            self.citas_agendadas.remove(cita)