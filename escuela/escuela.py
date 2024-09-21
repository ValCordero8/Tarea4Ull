from typing import List
from estudiantes.estudiante import Estudiantes
from grupos.grupo import Grupos
from materias.materia import Materias
from maestros.maestro import Maestros

from datetime import datetime
import random

class Escuela:
    lista_estudiantes: List[Estudiantes] = []
    lista_maestros: List[Maestros] = []
    list_grupos: List[Grupos] = []
    list_materias: List[Materias] = []

    def registrar_estudiante(self, estudiante: Estudiantes):
        self.lista_estudiantes.append(estudiante)

    def eliminar_estudiante(self, nombre: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.nombre == nombre:
                self.lista_estudiantes.remove(estudiante)
                return True
        return False

    def mostrar_estudiantes(self):
        return [estudiante.nombre for estudiante in self.lista_estudiantes]

    def registrar_maestro(self, maestro: Maestros):
        self.lista_maestros.append(maestro)

    def eliminar_maestro(self, nombre: str):
        for maestro in self.lista_maestros:
            if maestro.nombre == nombre:
                self.lista_maestros.remove(maestro)
                return True
        return False

    def generar_numero_control(self):
        ##L - 2024- 09- longiud lista estudiante + 1 +random(0,10000)
        numero_control = f"I{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{random(1,1000)} "
        return numero_control

    def mostrar_maestros(self):
        return [maestro for maestro in self.lista_maestros]
    
    def generar_numero_control_maestro(self, nombre: str, rfc: str):
        ### M-2004-DIA-random(500,5000)-Primeras dos letras nombre- Ultimas dos letras RFC- Longitud lista profes +1
        
        numero_control_maestro = f"M{datetime.now().year}{datetime.now().day}{random(500,5000)}{nombre[:2].upper()}{rfc[-2:].upper()}{len(self.lista_maestro) + 1}"
        return numero_control_maestro