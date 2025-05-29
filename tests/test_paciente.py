import unittest

from src.models.paciente import Paciente

class TestPaciente(unittest.TestCase):

    def test_crear_paciente(self):
        paciente = Paciente("12345678", "Pepito Juan", "15/05/1977")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertEqual(paciente.nombre, "Pepito Juan")
        self.assertEqual(paciente.fecha_nacimiento, "15/05/1977")

    def test_obtener_dni(self):
        paciente = Paciente("45366456", "Juan Pepito", "15/05/1977")
        self.assertEqual(paciente.obtener_dni(), "45366456")

    def test_str_paciente(self):
        paciente = Paciente("11223344", "Pepe Juan", "15/05/1977")
        expected = "Paciente: Pepe Juan, DNI: 11223344, FN: 15/05/1977"
        self.assertEqual(str(paciente), expected)

if __name__ == '__main__':
    unittest.main()
        