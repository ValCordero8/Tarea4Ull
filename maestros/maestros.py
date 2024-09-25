class Maestro:
    nombre: str
    apellido: str
    rfc: str
    sueldo: float
    
    def __init__(self,nombre: str, apellido: str, rfc: str, sueldo: float):
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo