class Materias:
    def __init__(self, nombre: str, creditos: int):
        self.nombre = nombre
        self.creditos = creditos

    def __repr__(self):
        return f"Materia(nombre={self.nombre}, creditos={self.creditos})"