from datetime import datetime
from .models.paciente import Paciente
from .models.medico import Medico
from .models.turno import Turno
from .models.receta import Receta
from .models.historia_clinica import HistoriaClinica
from .exceptions import PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError

class Clinica:
    def __init__(self):
        self.pacientes = {}
        self.medicos = {}
        self.turnos = []
        self.historias_clinicas = {}

    def agregar_paciente(self, paciente):
        dni = paciente.obtener_dni()
        self.pacientes[dni] = paciente
        self.historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico):
        matricula = medico.obtener_matricula()
        self.medicos[matricula] = medico
    
    def agendar_turno(self, dni, matricula, fecha_hora):
        if dni not in self.pacientes:
            raise PacienteNoExisteError(f"Paciente con DNI {dni} no existe")
    
        if matricula not in self.medicos:
            raise MedicoNoExisteError(f"Medico con matricula {matricula} no existe")
        
        for turno in self.turnos:
            if (turno.medico.obtener_matricula() == matricula and turno.fecha_hora == fecha_hora):
                raise TurnoDuplicadoError("Ya existe un turno para este doctor a esa fecha y hora")
            
        paciente = self.pacientes[dni]
        medico = self.medicos[matricula]
        turno = Turno(paciente, medico, fecha_hora)

        self.turnos.append(turno)
        self.historias_clinicas[dni].agregar_turno(turno)

    def emitir_receta(self, dni, matricula, medicamentos):
        if dni not in self.pacientes:
            raise PacienteNoExisteError(f"Paciente con DNI {dni} no existe")
    
        if matricula not in self.medicos:
            raise MedicoNoExisteError(f"Medico con matricula {matricula} no existe")
        
        paciente = self.pacientes[dni]
        medico = self.medicos[matricula]
        receta = Receta(paciente, medico, medicamentos)

        self.historias_clinicas[dni].agregar_receta(receta)
    
    def obtener_historia_clinica(self, dni):
        if dni not in self.historias_clinicas:
            raise PacienteNoExisteError(f"Paciente con DNI {dni} no existe")
        return self.historias_clinicas[dni]
    
    def obtener_turnos(self):
        return self.turnos.copy()
        