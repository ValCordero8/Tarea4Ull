class Materia:
    def __init__(self, nombre: str, maestro: str, descripcion: str, semestre: int, creditos: int, id: str):
        self.nombre = nombre
        self.maestro = maestro
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos
        self.id = id

    def mostrar_info_materias(self):
        info = (f"Instructor: {self.maestro}, "
                f"Nombre Completo: {self.nombre}, "
                f"Descripción: {self.descripcion}, "
                f"Semestre: {self.semestre}, "
                f"ID: {self.id}")
        return info
