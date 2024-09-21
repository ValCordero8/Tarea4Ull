from maestros.maestro import Maestros 
from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiantes
escuela = Escuela()

while True:
    print("""
          ***BIENVENIDO AL SISTEMA***
           Selecciona una opción:
          
           1.- Registrar estudiante
           2.- Registrar maestro
           3.- Eliminar estudiante
           4.- Eliminar maestro
           5.- Mostrar maestros
           6.- Mostrar estudiantes
           7.- Salir
           """)

    opcion = input("Ingresa una opción: ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del estudiante: ")
        edad = int(input("Ingresa la edad del estudiante: "))
        grado = input("Ingresa el grado del estudiante: ")
        escuela.registrar_estudiante(Estudiantes(nombre, edad, grado))
        print(f"Estudiante {nombre} registrado exitosamente.")

    elif opcion == "2":
        nombre = input("Ingresa el nombre del maestro: ")
        especialidad = input("Ingresa la especialidad del maestro: ")
        anio_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))
        rfc = input("Ingresa el RFC del maestro: ")
        nuevo_maestro = Maestros(nombre, especialidad, anio_nacimiento, rfc)
        escuela.registrar_maestro(nuevo_maestro)
        print(f"Médico {nombre} registrado exitosamente con número de control {nuevo_maestro.numero_control}.")

    elif opcion == "3":
        nombre = input("Ingresa el nombre del estudiante a eliminar: ")
        if escuela.eliminar_estudiante(nombre):
            print(f"Estudiante {nombre} eliminado exitosamente.")
        else:
            print(f"Estudiante {nombre} no encontrado.")

    elif opcion == "4":
        nombre = input("Ingresa el nombre del maestro a eliminar: ")
        if escuela.eliminar_maestro(nombre):
            print(f"Méaestro {nombre} eliminado exitosamente.")
        else:
            print(f"Maestro {nombre} no encontrado.")

    elif opcion == "5":
        maestros = escuela.mostrar_maestros()
        print("Maestros registrados:")
        for maestro in maestros:
            print(maestro)

    elif opcion == "6":
        estudiantes = escuela.mostrar_estudiantes()
        print("Estudiantes registrados:")
        for estudiante in estudiantes:
            print(estudiante)

    elif opcion == "7":
        print("Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, intenta de nuevo.")

    