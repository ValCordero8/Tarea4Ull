from typing import List
from estudiantes.estudiantes import Estudiante
from grupo.grupo import Grupo
from maestros.maestros import Maestro
from materias.materias import Materia
from datetime import datetime
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []    
    lista_grupos: List[Grupo] = []    
    lista_materias: List[Materia] = [] 
    lista_carreras: List[Carrera] = []  
    lista_semestres: List[Semestre] = [] 
    
    # Registrar estudiante
    def registrar_estudiante(self, estudiante: Estudiante):
        if estudiante not in self.lista_estudiantes:
            self.lista_estudiantes.append(estudiante)
            print(f"Estudiante registrado correctamente: {estudiante.nombre} {estudiante.apellido}")
        else:
            print("Estudiante ya registrado")
        
    # Generar n° de control para estudiantes
    def generar_numero_control(self) -> str:
        numero_control = f"I{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(1, 1000)}"
        return numero_control
    
    # Registrar maestro
    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)
    
    # Generar n° de control para maestros
    def generar_numero_control_maestro(self, nombre: str, rfc: str) -> str:
        numero_control_maestro = f"M{datetime.now().year}{datetime.now().day}{randint(500, 5000)}{nombre[:2].upper()}{rfc[-2:].upper()}{len(self.lista_maestros) + 1}"
        return numero_control_maestro
    
    # Generar ID de materia
    def generar_id_materia(self, nombre: str, semestre: int, creditos: int) -> str:
        id_materia = f"MT{nombre[-2:].upper()}{semestre}{creditos}{randint(100, 1000)}"
        return id_materia
        
    # Registrar materia
    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)
    
    # Listar estudiantes
    def listar_estudiantes(self):
        print("Estudiantes:")
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante()) 

    # Listar maestros
    def listar_maestros(self):
        print("Maestros:")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro()) 

    # Listar semestres
    def listar_semestres(self):
        print("Semestres:")
        for semestre in self.lista_semestres:
            print(semestre.info_semestre()) 

    # Listar grupos
    def listar_grupos(self):
        print("Grupos:")
        for grupo in self.lista_grupos:
            print(grupo.info_grupo()) 

    # Listar carreras
    def listar_carreras(self):
        print("Carreras:")
        for carrera in self.lista_carreras:
            print(carrera.info_carrera()) 

    # Listar materias
    def listar_materias(self):
        print("Materias:")
        for materia in self.lista_materias:
            print(materia.mostrar_info_materias()) 

    # Eliminar estudiante
    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                return
        print(f"No se encontró estudiante con n° control: {numero_control}")

    # Eliminar maestro
    def eliminar_maestro(self, numero_control_maestro: str):
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control_maestro:
                self.lista_maestros.remove(maestro)
                print("Maestro eliminado")
                return
        print(f"No se encontró maestro con n° control: {numero_control_maestro}")

    # Eliminar materia
    def eliminar_materia(self, id: str):
        for materia in self.lista_materias:
            if materia.id == id:
                self.lista_materias.remove(materia)
                print("Materia eliminada")
                return
        print(f"No se encontró materia con ese ID: {id}")
