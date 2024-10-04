from typing import List
from semestre.semestre import Semestre
from  random import randint


class Carrera:
    matricula: str
    nombre: str
    no_semestre: int
    semestres: List[Semestre]

    def __init__(self, nombre:str):
        self.matricula: self.generar_id_carrera[nombre]
        self.nombre: nombre

    def generar_id_carrera(self, nombre: int) -> str:
        return f"{nombre}-{randint(0,100000)}-{randint(0,100000)}"
    
    def registrar_semsetre(self, semestre: Semestre):
        self.semestres.append()

    def info_carrera(self):
        print("CARRERAS")
        info = f"Nombre: {self.nombre}, Matricula: {self.matricula}, N. Carrera: {self.no_semestre}"
        return info