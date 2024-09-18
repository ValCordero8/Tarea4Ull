
from paciente.paciente import Paciente
from hospital.hospital import Hospital
from medico.medico import Medico

hospital = Hospital()

while True:
    print("""
          ***BIENVENIDO AL SISTEMA***
           Selecciona una opcion:
          
           1.- Registrar paciente
           2.- Registrar medico
           3.- Eliminar paciente
           4.- Eliminar medico
           5.- Mostrar medicos
           6.- Mostrar pacientes
           7.- Mostrar pacientes menores de edad
           8.- Mostrar pacientes mayores de edad
           9.- Salir
          
           """)
    opcion = input("Ingresa una opcion: ")

    if opcion == "1":
        print("Seleccionaste la opcion para registrar paciente")
        
        nombre = input("Ingresa el nombre: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
        peso = float(input("Ingresa el peso: "))
        estatura = float(input("Ingresa la estatura: "))
        direccion = input("Ingresa la direccion: ")
        
        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente=paciente)
        print("\nPaciente registrado")
        
        
    elif opcion == "2":
        nombre = input("Ingresa el nombre del medico: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento del medico: "))
        rfc = input("Ingresa el peso del medico: ")
        direccion = input("Ingresa la direccion del medico: ")
        
        medico = Medico(nombre = nombre, ano_nacimiento=ano_nacimiento, rfc=rfc, direccion=direccion)
        hospital.registrar_medico(medico=medico)
        print("\nMedico regitrado")
    
    elif opcion == "3":
        id = int(input("Ingresa el id del paciente a eliminar: "))
        hospital.eliminar_paciente(id)
        print("\nPaciente eliminado")
    
    elif opcion == "4":
        id = int(input("Ingresa el id del medico a eliminar: "))
        hospital.eliminar_medico(id=id)
        print("\nMedico eliminado")
       
    elif opcion == "5":
        hospital.mostrar_medicos()   
       
    elif opcion == "6":
        hospital.mostrar_pacientes()
         
    elif opcion == "7":
        hospital.mostrar_pacientes_menores_edad()
        
    elif opcion == "8":
        hospital.mostrar_pacientes_mayores_edad()
        
    elif opcion == "9":
        print("\nSalio del sistema")
        break