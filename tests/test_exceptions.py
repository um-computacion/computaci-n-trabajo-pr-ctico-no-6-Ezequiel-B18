import unittest

from src.exceptions import PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError

class TestExceptions(unittest.TestCase):
    
    def test_paciente_no_existe_error(self):
        with self.assertRaises(PacienteNoExisteError):
            raise PacienteNoExisteError("Paciente con DNI 12345678 no existe")
    
    def test_medico_no_existe_error(self):
        with self.assertRaises(MedicoNoExisteError):
            raise MedicoNoExisteError("Medico con Matricula MN12345")
        
    def test_paciente_no_existe_error(self):
        with self.assertRaises(TurnoDuplicadoError):
            raise TurnoDuplicadoError("Ya existe un turno para este medico en ese dia y hora")
        
if __name__ == '__main__':
    unittest.main()