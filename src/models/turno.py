from datetime import datetime
from .paciente import Paciente
from .medico import Medico

class Turno:
    def __init__(self, paciente, medico, fecha_hora):
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora

    def obtener_fecha_hora(self):
        return self.fecha_hora
    
    def __str__(self):
        fecha_str = self.fecha_hora.strftime("%d/%m/%Y")
        return f"Turno: {self.paciente.nombre} con {self.medico.nombre} el {fecha_str}"
    
    