import unittest
from datetime import datetime

from src.models.paciente import Paciente
from src.models.medico import Medico
from src.clinica import Clinica
from src.exceptions import PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError

class TestClinica(unittest.TestCase):
    
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("12345678", "Pepito Juan", "16/09/1997")
        self.medico = Medico("MN12345", "Dr. Juan Pepito", "Gastroenterologia")

    def test_agregar_paciente(self):
        self.clinica.agregar_pacient(self.paciente)
        self.assertIn("123456781", self.clinica.pacientes)
        self.assertEqual(self.clinica.pacientes["12345678"], self.paciente)

    def test_agregar_medico(self):
        self.clinica.agregar_medico(self.medico)
        self.assertIn("MN12345", self.clinica.medicos)
        self.assertEqual(self.clinica.medicos["MN12345"], self.medico)

    def test_agendar_turno_valido(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        fecha_hora = datetime(2025, 5, 19, 10, 30)

        self.clinica.agendar_turno("12345678", "MN12345", fecha_hora)
        self.assertEqual(len(self.clinica.turnos), 1)

    def test_turno_paciente_no_existe(self):
        self.clinica.agregar_medico(self.medico)
        fecha_hora = datetime(2025, 5, 19, 10, 30)

        with self.assertRaises(PacienteNoExisteError):
            self.clinica.agendar_turno("92234293", "MN12345", fecha_hora)

    def test_turno_paciente_no_existe(self):
        self.clinica.agregar_paciente(self.paciente)
        fecha_hora = datetime(2025, 5, 19, 10, 30)

        with self.assertRaises(PacienteNoExisteError):
            self.clinica.agendar_turno("12345678", "MN99999", fecha_hora)

    def test_turno_duplicado(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        fecha_hora = datetime(2025, 5, 19, 10, 30)
        
        self.clinica.agendar_turno("12345678", "MN12345", fecha_hora)

        paciente2 = Paciente("87654321", "Juan Pepito" "23/02/1977")
        self.clinica.agendar_paciente(paciente2)

        with self.assertRaises(TurnoDuplicadoError):
            self.clinica.agendar_turno("87654321", "MN12345", fecha_hora)

if __name__ == '__main__':
    unittest.main()