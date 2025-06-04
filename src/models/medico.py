'''
**Atributos privados:**
- `matricula` (str)
- `nombre` (str)
- `especialidad` (str)

**Métodos:**
- `obtener_matricula() → str`
- `__str__() → str`
'''
class Medico:
    def __init__(self, matricula, nombre, especialidad):
        self._matricula = matricula
        self.nombre = nombre
        self.especialidad = especialidad

    def obtener_matricula(self):
        return self._matricula
    
    def __str__(self):
        return f"{self.nombre}, {self.especialidad}, Matricula: {self._matricula}"