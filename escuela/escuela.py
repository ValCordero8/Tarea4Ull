from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from coordinador.coordinador import Coordinador
from usuario.usuario import Usuario
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from datetime import datetime
from random import randint

class Escuela:
    lista_usuarios: List[Usuario] = []
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []
    lista_carreras: List[Carrera] = []
    lista_semestres: List[Semestre] = []

    def __init__(self):
        # Crear un usuario por default
        coordinador = Coordinador(
            numeroControl="12345",
            nombre="Edson",
            apellido="Medina",
            rfc="MEDINA123",
            sueldo=100000,
            anios_antiguedad=10,
            contrasenia="123*",
        )

        self.lista_usuarios.append(coordinador)

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_usuarios.append(estudiante)
        self.lista_estudiantes.append(estudiante)

    def registrar_maestro(self, maestro: Maestro):
        self.lista_usuarios.append(maestro)
        self.lista_maestros.append(maestro)

    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)

    def registrar_carrera(self, carrera: Carrera):
        self.lista_carreras.append(carrera)

    def registrar_grupo(self, grupo: Grupo):
        id_semestre = grupo.id_semestre

        for semestre in self.lista_semestres:
            if id_semestre == semestre.id:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break

        self.lista_grupos.append(grupo)

    def registrar_semestre(self, semestre: Semestre):
        id_carrera = semestre.id

        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break

        self.lista_semestres.append(semestre)

    def listar_estudiantes(self):
        print("\n** ESTUDIANTES **")

        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())

    def listar_maestros(self):
        print("\n** MAESTROS **")

        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())

    def listar_materias(self):
        print("\n** MATERIAS **")

        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())

    def listar_carreras(self):
        print("*** CARRERAS ***")
        
        for carrera in self.lista_carreras:
            print(carrera.nombre)

    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                return

        print(f"\nNo se encontró el estudiante con numero de control: {numero_control}")

    def generar_numero_control(self):
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_estudiantes) + 1
        aleatorio = randint(0, 10000)

        numero_control = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
        
        return numero_control

    def generar_numero_control_maestro(self, nombre: str, rfc: str, ano_nacimiento: int) -> str:
        dia_actual = datetime.now().day
        aleatorio = randint(500, 5000)
        primeras_letras_nombre = nombre[:2].upper()
        ultimas_letras_rfc = rfc[-2:].upper()
        longitud_mas_uno = len(self.lista_maestros) + 1

        numero_control = f"M-{ano_nacimiento}{dia_actual}{aleatorio}{primeras_letras_nombre}{ultimas_letras_rfc}{longitud_mas_uno}"
        
        return numero_control

    def validar_inicio_sesion(self, numero_control: str, contrasenia: str):
        for usuario in self.lista_usuarios:
            if usuario.numero_control == numero_control:
                if usuario.contrasenia == contrasenia:
                    return usuario
                
        return None
    
    def buscar_estudiante_por_numero_control(self, numero_control_estudiante: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control_estudiante:
                return estudiante
            
        return None
    
    def buscar_maestro_por_numero_control(self, numero_control_maestro: str):
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control_maestro:
                return maestro
            
        return None
    
    def buscar_grupo_por_id(self, id_grupo: str):
        for grupo in self.lista_grupos:
            if grupo.id == id_grupo:
                return grupo
            
        return None

    
    def registrar_estudiante_en_grupo(self, numero_control_estudiante: str, id_grupo: str):
        estudiante = self.buscar_estudiante_por_numero_control(
            numero_control_estudiante=numero_control_estudiante
        )

        if estudiante is None:
            print("No se encontró un estudiante con el número de control proporcionado")
            return
        
        grupo = self.buscar_grupo_por_id(id_grupo=id_grupo)

        if grupo is None:
            print("No se encontró un grupo con ID proporcionado")
            return
        
        grupo.registrar_estudiante(estudiante=estudiante)
        print("Estudiante asignado el grupo correctamente")

    def ver_grupos_asignados_a_estudiante(self, numero_control_estudiante: str):
        estudiante = self.buscar_estudiante_por_numero_control(
            numero_control_estudiante=numero_control_estudiante
        )

        if estudiante is None:
            print("No se encontró un estudiante con el número de control proporcionado")
            return
        
        for grupo in self.lista_grupos:
            grupo.mostrar_info_grupo_para_estudiante()