from typing import List
from paciente.paciente import Paciente
from consultas.consulta import Consulta
from medico.medico import Medico

class Hospital:
    pacientes: List[Paciente] = []
    medicos: List[Medico] = []
    consultas: List[Consulta] = []

    def registrar_consulta(self, id_paciente, id_medico):
        if not self.validar_cantidad_usuarios():
            return
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el médico o el paciente")
            return
        
        print("Continuamos con el registro")

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def registrar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_pacientes(self):
        print("*** Pacientes en el Sistema ***")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()
    
    def mostrar_medicos(self):
        print("*** Médicos en el Sistema ***")
        for medico in self.medicos:
            medico.mostrar_informacion()

    # Método para mostrar todos los pacientes menores de edad (suponemos menor de 18 años)
    def mostrar_pacientes_menores_edad(self):
        print("*** Pacientes menores de edad ***")
        for paciente in self.pacientes:
            if paciente.ano_nacimiento > 2006:
                paciente.mostrar_informacion()

    # Método para mostrar todos los pacientes mayores de edad (18 años o más)
    def mostrar_pacientes_mayores_edad(self):
        print("*** Pacientes mayores de edad ***")
        for paciente in self.pacientes:
            if paciente.ano_nacimiento <= 2006:
                paciente.mostrar_informacion()

    # Método para eliminar un paciente por su ID
    def eliminar_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                self.pacientes.remove(paciente)
                print(f"Paciente con ID {id_paciente} ha sido eliminado.")
                return
        print(f"Paciente con ID {id_paciente} no encontrado.")

    # Método para eliminar un médico por su ID
    def eliminar_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                self.medicos.remove(medico)
                print(f"Médico con ID {id_medico} ha sido eliminado.")
                return
        print(f"Médico con ID {id_medico} no encontrado.")


    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
  
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes) == 0:
            print("No puedes registra una consulta, no existen pacientes")
            return False
        
        if len(self.medicos) == 0:
            print("No puedes registra una consulta, no existen médicos")
            return False
        
        return True