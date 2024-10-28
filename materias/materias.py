from maestros.maestros import Maestro




class Materia:

    nombre: str
    descripcion: str
    id_semestre: str
    creditos : int
    maetsro: Maestro



    def __init__(self, nombre: str, maestro: str, descripcion: str, semestre: int, creditos: int, id: str , ):
        self.nombre = nombre
        self.maestro = maestro
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos
        self.id = id
        self.maestro = maestro

    def mostrar_info_materia(self):
        info = (f"Maestro: {self.maestro}, "
                f"Nombre Completo: {self.nombre}, "
                f"Descripción: {self.descripcion}, "
                f"Semestre: {self.semestre}, "
                f"ID: {self.id}")
        return info
