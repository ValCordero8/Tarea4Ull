from typing import List
from estudiantes.estudiantes import Estudiante
from datetime import datetime
from maestros.maestros import Maestro
from materias.materias import Materia
from random import randint

class Grupo: 
    id: str
    estudiantes: List[Estudiante] = []
    materia: List [Materia] = []
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
    def registrar_estudiante(self, estdudiante: Estudiante)
        self.estudiantes.append(estdudiante)

    def registrar_materia(self, materia: Materia)
        self.materias.append(Materia)
        
  

    def mostrar_info_grupo_para_estudiante(self):
       
        print("Informacion del frupo {self.tipo}, del semestre {self.id_semestre}")
        for materia in self.materia:
         print(materia.mostrar_info_materia)

