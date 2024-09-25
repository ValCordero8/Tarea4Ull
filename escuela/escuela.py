from typing import List
from estudiantes.estudiantes import Estudiante
from grupo.grupo import Grupo
from maestros.maestros import Maestro
from materias.materias import Materia
from datetime import datetime
from random import randint
from typing import List

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestro: List[Maestro] = []    
    lista_grupos: List[Grupo] = []    
    lista_materias: List[Materia] = []  
    
    #lista materias
    
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append  
        
    def generar_numero_control(self):
        ##L - 2024- 09- longiud lista estudiante + 1 +random(0,10000)
        numero_control = f"I{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(1,1000)} "
        return numero_control
    
    def registrar_maestro(self, maestros: Maestro):
        self.lista_maestro.append
    
    def generar_numero_control_maestro(self, nombre: str, rfc: str):
        ### M-2004-DIA-random(500,5000)-Primeras dos letras nombre- Ultimas dos letras RFC- Longitud lista profes +1
        
        numero_control_maestro = f"M{datetime.now().year}{datetime.now().day}{randint(500,5000)}{nombre[:2].upper()}{rfc[-2:].upper()}{len(self.lista_maestro) + 1}"
        return numero_control_maestro
    
    def generar_id_maestro(self, nombrem: str, semestre: int, creditos: int):
        id = f"MT{nombrem[-2:].upper()}{semestre}{creditos}{randint(100,1000)}"
        #"MT {ultimos dos digitos del nombre, semestre, cantidad creditos, random del 1-1000}"
        return id
        
    def registrar_materia(self, materia: Materia):
        self.lista_materias.append