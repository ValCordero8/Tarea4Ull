from typing import List
from estudiantes.estudiantes import Estudiante
from datetime import datetime
from maestros.maestros import Maestro
from materias.materias import Materia
from random import randint

class Grupo: 
    id: int
    estudiantes: List[Estudiante] = []
    materias: List[Materia] = []
    maestros: List[Maestro] = []
    tipo: chr
    id_semestre: str

    def __init__(self, tipo, id_semestre):
        self.id = self.generar_id_grupo[tipo]
        self.tipo = tipo
        self.id_semestre = id_semestre
    
    def generar_id_grupo(self, tipo: chr) -> str:
        return f"{tipo}-{randint(0,100000)}-{randint(0,100000)}"
    
    def info_grupo(self):  
        print("GRUPO")
        info = f"ID: {self.id}, TIPO: {self.tipo}, ID SEMESTRE: {self.id_semestre}"
        return info