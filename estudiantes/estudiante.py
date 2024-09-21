from datetime import datetime

class Estudiantes:
    numero_control: str
    nombre: str
    apellido: str
    curp: str
    fecha_nacimiento: datetime

    def __init__(self, nombre: str, edad: int, apellido: str, curp: int, fecha_nacimiento: datetime):
        self.numero_control = "L22121047"
        self.nombre = nombre
        self.apellido = apellido
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento