'''### ✅ Turno

**Atributos privados:**
- `paciente` (Paciente)
- `medico` (Medico)
- `fecha_hora` (datetime)

**Métodos:**
- `obtener_fecha_hora() → datetime`
- `__str__() → str` (formato dd/mm/aaaa)'''

import unittest 
from datetime import datetime

from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.turno import Turno

class TestTurno(unittest.TestCase):
    
    def setUp(self):
        self.paciente = Paciente("12345678", "Pepito Juan", "15/05/1977")
        self.medico = Medico("MN12345", "Dr. Juan Pepito", "Cardiologia")
        self.fecha_hora = datetime(2025, 6, 15, 10, 30)

    def test_crear_turno(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora)
        self.assertEqual(turno.paciente, self.paciente)
        self.assertEqual(turno.medico, self.medico)
        self.assertEqual(turno.fecha_hora, self.fecha_hora)

    def test_obtener_fecha_hora(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora)
        self.assertEqual(turno.obtener_fecha_hora(), self.fecha_hora)

    def test_str_turno(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora)
        expected = "Turno: Pepito Juan con Dr. Juan Pepito el 15/06/2025"
        self.assertEqual(str(turno), expected)

if __name__ == '__main__':
    unittest.main()