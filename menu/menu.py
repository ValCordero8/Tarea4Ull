from escuela.escuela import Escuela
from estudiantes.estudiantes import Estudiante
from materias.materias import Materia
from semestre.semestre import Semestre
from maestros.maestros import Maestro
from grupo.grupo import Grupo
from carrera.carrera import Carrera
from datetime import datetime

class Menu:
    escuela = Escuela()
    usuario_estudiante: str = "juan123"
    contrasenia_estudiante: str = "1234"

    usuario_maestro: str= "hilary123"
    contrasenia_maestro: str = "5432"

    def login(self):
        intentos = 0
        while intentos < 3:
            print("Bienvenido")
            print("Inicie sesión")

            nombre_usuario = input("Ingresa usuario: ")
            contrasenia_usuario = input("Ingresa contraseña: ")

            if nombre_usuario == self.usuario_estudiante:
                if contrasenia_usuario == self.contrasenia_estudiante:
                    self.menu_estudiante()
                else:
                    intentos = self.mostrar_intento_sesion_fallido(intentos)

            elif nombre_usuario == self.usuario_maestro:
                if contrasenia_usuario == self.contrasenia_maestro:
                    self.menu_maestro()
                else:
                    intentos = self.mostrar_intento_sesion_fallido(intentos)

            else:
                intentos = self.mostrar_intento_sesion_fallido(intentos)

        print("Máximos intentos alcanzados")

    def mostrar_intento_sesion_fallido(self, intentos):
        print("Usuario o contraseña incorrectos")
        intentos += 1
        return intentos

    def menu_estudiante(self):
        print("MENU ESTUDIANTE")

    def menu_maestro(self):
        print("MENU MAESTRO")

    def mostrar_menu(self):
        while True:
            print("*** MINDBOX ***")
            print("1. Registrar estudiante")
            print("2. Registrar maestro")
            print("3. Registrar materia")
            print("4. Registrar grupo")
            print("5. Registrar carrera")
            print("6. Listar estudiantes")
            print("7. Listar maestros")
            print("8. Listar materias")
            print("9. Listar grupos")
            print("10. Eliminar estudiante")
            print("11. Eliminar maestro")
            print("12. Eliminar materia")
            print("13. Eliminar grupo")
            print("14. Registrar semestre")
            print("15. Listar semestres")
            print("16. Listar carreras")
            print("17. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nombre = input("Ingresa nombre del estudiante: ")
                numero_control = input("Ingresa número de control: ")
                estudiante = Estudiante(nombre=nombre, numero_control=numero_control)
                self.escuela.registrar_estudiante(estudiante=estudiante)

            elif opcion == "2":
                nombre = input("Ingresa nombre del maestro: ")
                id_maestro = input("Ingresa ID del maestro: ")
                maestro = Maestro(nombre=nombre, id_maestro=id_maestro)
                self.escuela.registrar_maestro(maestro=maestro)

            elif opcion == "3":
                nombre = input("Ingresa nombre de la materia: ")
                id_materia = input("Ingresa ID de la materia: ")
                materia = Materia(nombre=nombre, id_materia=id_materia)
                self.escuela.registrar_materia(materia=materia)

            elif opcion == "4":
                tipo = input("Ingresa tipo de grupo (A/B): ")
                id_semestre = input("ID semestre: ")
                grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
                self.escuela.registrar_grupo(grupo=grupo)

            elif opcion == "5":
                nombre = input("Ingresa nombre de la carrera: ")
                carrera = Carrera(nombre=nombre)
                self.escuela.registrar_carrera(carrera=carrera)

            elif opcion == "6":
                self.escuela.listar_estudiantes()

            elif opcion == "7":
                self.escuela.listar_maestros()

            elif opcion == "8":
                self.escuela.listar_materias()

            elif opcion == "9":
                self.escuela.listar_grupos()

            elif opcion == "10":
                numero_control = input("Ingresa número de control del estudiante: ")
                self.escuela.eliminar_estudiante(numero_control=numero_control)

            elif opcion == "11":
                id_maestro = input("Ingresa ID del maestro: ")
                self.escuela.eliminar_maestro(id_maestro=id_maestro)

            elif opcion == "12":
                id_materia = input("Ingresa ID de la materia: ")
                self.escuela.eliminar_materia(id=id_materia)

            elif opcion == "13":
                id_grupo = input("Ingresa ID del grupo: ")
                self.escuela.eliminar_grupo(id_grupo=id_grupo)

            elif opcion == "14":
                numero = input("Ingresa número del semestre: ")
                id_carrera = input("Ingresa ID de la carrera: ")
                semestre = Semestre(numero=numero, id_carrera=id_carrera)
                self.escuela.registrar_semestre(semestre=semestre)

            elif opcion == "15":
                self.escuela.listar_semestres()

            elif opcion == "16":
                self.escuela.listar_carreras()

            elif opcion == "17":
                print("Hasta luego")
                break
