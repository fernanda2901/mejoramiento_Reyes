class CitaMedica():
    # el costructor d ela clase, se ejecuta al crear una instacia de citasmedicas 
    def _init_(self, paciente, medico, fecha, hora, motivo):
       # Inicialización de atributos de la cita con los datos proporcionados
        self.paciente = paciente # Instancia de la clase Paciente asociada a la cita
        self.medico = medico   # Instancia de la clase Medico asociada a la cita
        self.fecha = fecha     # Fecha de la cita (cadena)
        self.hora = hora        # Hora de la cita (cadena)
        self.motivo = motivo   # Motivo de la cita (cadena)

    def obtenerInformacionCita(self): # metodo para obtener informacion completa de la cita como una cadena 
        #Retorna una cadena con la información de la cita, incluyendo paciente, médico, especialidad, fecha, hora y motivo
        return f"Paciente: {self.paciente.nombre}, Médico: {self.medico.nombre}, Especialidad: {self.medico.especialidad}, Fecha: {self.fecha}, Hora: {self.hora}, Motivo: {self.motivo}"