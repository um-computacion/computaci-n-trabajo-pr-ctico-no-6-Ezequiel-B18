'''### ✅ Medico

**Atributos privados:**
- `_matricula` (str)
- `nombre` (str)
- `especialidad` (str)

**Métodos:**
- `obtener_matricula() → str`
- `__str__() → str`'''
import unittest

from src.models.medico import Medico

class TestMedico(unittest.TestCase):
    
    def test_crear_medico(self):
        medico = Medico("MN12345", "Dr. Pepito Juan", "Cardiologia")
        self.assertEqual(medico.nombre, "Dr. Pepito Juan")
        self.assertEqual(medico.especialidad, "Cardiologia")

    def test_obtener_matricula(self):
        medico = Medico("MN67890", "Dra. Juana", "Neurologia")
        self.assertEqual(medico.obtener_matricula(), "MN67890")

    def test_str_medico(self):
        medico = Medico("MN67890", "Dr. Juan Pepito", "Neurologia")
        expected = "Dr. Juan Pepito, Neurologia, Matricula: MN67890"
        self.assertEqual(str(medico), expected)

if __name__ == '__main__':
    unittest.main()