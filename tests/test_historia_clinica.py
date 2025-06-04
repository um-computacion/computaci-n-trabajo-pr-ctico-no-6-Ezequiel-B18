import unittest
from datetime import datetime

from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.turno import Turno
from src.models.receta import Receta
from src.models.historia_clinica import HistoriaClinica

class TestHistoriaClinica(unittest.TestCase):
    
    def setUp(self):
        self.paciente = Paciente("12345678", "Pepito Juan", "15/05/1977")
        self.medico = Medico("MN12345", "Dr. Juan Pepito", "Oftalmologia")
        self.turno = Turno(self.paciente, self.medico, datetime(2025, 6, 15, 10, 30))
        self.receta = Receta(self.paciente, self.medico, ["Aspirina 100mg"])

    def test_crear_historia_clinica(self):
        historia = HistoriaClinica(self.paciente)
        self.assertEqual(len(historia.turnos), 0)
        self.assertEqual(historia.paciente, self.paciente)

    def test_agregar_turno(self):
        historia = HistoriaClinica(self.paciente)
        historia.agregar_turno(self.turno)
        self.assertEqual(len(historia.turnos), 1)
        self.assertEqual(historia.turnos[0], self.turno)

    def test_agregar_receta(self):
        historia = HistoriaClinica(self.paciente)
        historia.agregar_receta(self.receta)
        self.assertEqual(len(historia.recetas), 1)
        self.assertEqual(historia.recetas[0], self.receta)

    def test_obtener_turnos(self):
        historia = HistoriaClinica(self.paciente)
        historia.agregar_turno(self.turno)
        turnos = historia.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0], self.turno)

    def test_obtener_recetas(self):
        historia = HistoriaClinica(self.paciente)
        historia.agregar_receta(self.receta)
        recetas = historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertEqual(recetas[0], self.receta)
    
    def test_str_historia_clinica_vacia(self):
        historia = HistoriaClinica(self.paciente)
        resultado = str(historia)
        
        self.assertIn("Historia Clinica de Pepito Juan", resultado)
        self.assertIn("DNI: 12345678", resultado)
        self.assertIn("Turnos (0):", resultado)
        self.assertIn("Recetas (0):", resultado)

    def test_str_historia_clinica_con_datos(self):
        historia = HistoriaClinica(self.paciente)
        historia.agregar_turno(self.turno)
        historia.agregar_receta(self.receta)
        
        resultado = str(historia)
        
        self.assertIn("Historia Clinica de Pepito Juan", resultado)
        self.assertIn("DNI: 12345678", resultado)
        self.assertIn("Turnos (1):", resultado)
        self.assertIn("Recetas (1):", resultado)

if __name__ == '__main__':
    unittest.main()