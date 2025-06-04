import unittest
from datetime import datetime

from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.receta import Receta

class TestReceta(unittest.TestCase):

    def crear_receta(self):
        self.paciente = Paciente("12345678", "Juan Pepito", "15/03/1997")
        self.medico = Medico("MN12345", "Dr. Pepito Juan", "Cardiologia")
        self.medicamentos = ["Aspirina 100mg", "Omeprazol 20mg"]

    def test_crear_receta(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        self.assertEqual(receta.paciente, self.paciente)
        self.assertEqual(receta.medico, self.medico)
        self.assertEqual(receta.medicamentos, self.medicamentos)
        self.assertIsInstance(receta._fecha, datetime)

    def test_str_receta(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        self.assertIn("Receta para Juan Pepito", str(receta))
        self.assertIn("Dr. Pepito Juan", str(receta))
        self.assertIn("Aspirina 100mg", str(receta))

if __name__ == '__main__':
    unittest.main()