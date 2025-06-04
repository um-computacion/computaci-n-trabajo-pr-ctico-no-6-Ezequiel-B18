from datetime import datetime
from .paciente import Paciente
from .medico import Medico

class Receta:
    def __init__(self, paciente, medico, medicamentos):
        self.paciente = paciente
        self.medico = medico
        self.medicamentos = medicamentos
        self._fecha = datetime.now()

    def __str__(self):
        fecha_str = self._fecha.strftime("%d/%m/%Y")
        medicamentos_str = "\n".join([f"-{med}" for med in self.medicamentos])
        return f"Receta para {self.paciente.nombre} \nMedico: {self.medico.nombre}\nFecha: {fecha_str}\nMedicamentos:\n{medicamentos_str}"