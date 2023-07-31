class Paciente():
    # Constructor de la clase, se ejecuta al crear una instancia de Paciente
    def _init_(self, nombre, especialidad):
         # Inicialización de atributos del paciente con los datos proporcionados
        self.nombre = nombre  # Nombre del paciente (cadena)
        self.especialidad = especialidad # # Especialidad del paciente (cadena)
        self.citas_registradas = []   # Lista de citas médicas registradas por el paciente

    def registrar_cita(self, cita): #registrar una nueva cita médica
        self.citas_registradas.append(cita) # Agregar la cita a la lista de citas registradas

    def consultar_citas_registradas(self): #consultar las citas médicas registradas por el paciente
        return self.citas_registradas   # Devuelve la lista de citas registradas por el paciente
    
    def eliminar_cita_propia(self, cita): #eliminar una cita médica registrada por el paciente
        if cita in self.citas_registradas:
            self.citas_registradas.remove(cita) # Eliminar la cita de la lista de citas registradas
            print("¡Cita médica eliminada exitosamente!")
        else:
            print("La cita no se encontró en las citas registradas.")