'''
**Atributos privados:**
- `_dni` (str)
- `nombre` (str)
- `fecha_nacimiento` (str)

**Métodos:**
- `obtener_dni() → str`
- `__str__() → str`
'''
class Paciente:
    def __init__(self, dni, nombre, fecha_nacimiento):
        self._dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self):
        return self._dni
    
    def __str__(self):
        return f"Paciente: {self.nombre}, DNI: {self._dni}, FN: {self.fecha_nacimiento}"