from typing import List
from materias.materias import Materia
from grupo.grupo import Grupo
from random import randint

class Semestre:
    id: str
    numero: int
    id_carrera: str
    materias: List[Materia]
    grupo: List[Grupo]

    def __init__(self, numero: int, id_carrera: str):
        self.id = self.generar_id_semestre(numero)
        self.id_carrera = id_carrera
        self.numero = numero
        self.materias = []  # Inicializa la lista de materias
        self.grupo = []     # Inicializa la lista de grupos

    def generar_id_semestre(self, numero_semestre: int) -> str:
        return f"{numero_semestre}-{randint(0, 100000)}-{randint(0, 100000)}"

    def registrar_grupo_en_semestre(self, grupo: Grupo):
        self.grupo.append(grupo)

    def info_semestre(self): 
        print("Semestre") 
        info = f"ID: {self.id}, Número: {self.numero}, ID Carrera: {self.id_carrera}"
        return info
