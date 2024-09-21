class Maestros:
    def __init__(self, nombre: str, especialidad: str, rfc: str):
        self.nombre = nombre
        self.especialidad = especialidad
        self.rfc = rfc

    def __repr__(self):
        return f"Maestro(nombre={self.nombre}, especialidad={self.especialidad})"