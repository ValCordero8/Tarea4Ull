from typing import List
from estudiantes.estudiantes import Estudiante
from grupo.grupo import Grupo
from maestros.maestros import Maestro
from materias.materias import Materia
from datetime import datetime
from  random import randint
from typing import List

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestro: List[Maestro] = []    
    lista_grupos: List[Grupo] = []    
    lista_materias: List[Materia] = []  
    
    #lista materias
    
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
        
    def generar_numero_control(self):
        ##L - 2024- 09- longiud lista estudiante + 1 +random(0,10000)
        numero_control = f"I{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(1,1000)} "
        return numero_control
    
    def registrar_maestro(self, maestros: Maestro):
        self.lista_maestro.append(maestros)
    
    def generar_numero_control_maestro(self, nombre: str, rfc: str):
        ### M-2004-DIA-random(500,5000)-Primeras dos letras nombre- Ultimas dos letras RFC- Longitud lista profes +1
        
        numero_control_maestro = f"M{datetime.now().year}{datetime.now().day}{randint(500,5000)}{nombre[:2].upper()}{rfc[-2:].upper()}{len(self.lista_maestro) + 1}"
        return numero_control_maestro
    
    def generar_id_materia(self, nombrem: str, semestre: int, creditos: int):
        id = f"MT{nombrem[-2:].upper()}{semestre}{creditos}{randint(100,1000)}"
        #"MT {ultimos dos digitos del nombre, semestre, cantidad creditos, random del 1-1000}"
        return id
        
    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)
    
    def listar_estudiantes(self):
        print("Estudiantes")
        for estudiante in self.lista_estudiantes:
            print (estudiante.mostrar_info_estudiante()) 

    def listar_maestros(self):
        print("Mestros")
        for maestro in self.lista_maestro:
            print (maestro.mostrar_info_maestro()) 

    def listar_materia(self):
        print("Materias")
        for materias in self.lista_materias:
            print (materias.mostrar_info_materias()) 

    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("estudiante eliminado")
                return
        print(f"no se encontro estudiante con no. control: {numero_control}")

    def eliminar_maestro(self, numero_control_maestro: str):
        for maestro in self.lista_estudiantes:
            if maestro.numero_control == numero_control_maestro:
                self.lista_maestro.remove(maestro)
                print("estudiante eliminado")
                return
        print(f"no se encontro maestro con no. control: {numero_control_maestro}")

    def eliminar_materia(self, id: str):
        for materia in self.lista_materias:
            if materia.id == id:
                self.lista_materias.remove(materia)
                print("materia eliminada")
                return
        print(f"no se encontro materia con ese id: {id}")