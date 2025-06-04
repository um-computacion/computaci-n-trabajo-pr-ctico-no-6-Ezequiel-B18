from .paciente import Paciente
from .turno import Turno
from .receta import Receta

class HistoriaClinica:
    def __init__(self, paciente):
        self.paciente = paciente
        self.turnos = []
        self.recetas = []

    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def agregar_receta(self, receta):
        self.recetas.append(receta)

    def obtener_turnos(self):
        return self.turnos.copy()
    
    def obtener_recetas(self):
        return self.recetas.copy()
    
    def __str__(self):
        resultado = f"Historia Clinica de {self.paciente.nombre}\n"
        resultado += f"DNI: {self.paciente.obtener_dni()}\n\n"

        resultado += f"Turnos ({len(self.turnos)}):\n"
        if self.turnos:
            for turno in self.turnos:
                resultado += f"- {turno}\n"
        else:
            resultado += "- No hay turnos registrados\n"

        resultado += f"\nRecetas ({len(self.recetas)}):\n"
        if self.recetas:
            for receta in self.recetas:
                resultado += f"- {receta}\n"
        else:
            resultado += "- No hay recetas registradas\n"

        return resultado.strip()