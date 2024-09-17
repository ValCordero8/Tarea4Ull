

from paciente import Paciente
from medico import Medico
from hospital import Hospital
from consulta import Consulta

hospital = Hospital()

paciente = Paciente("Juan", 2004, 76, 1.78, "Avenida Madero") # 5
paciente_dos = Paciente("Jonathan", 2008, 70, 1.90, "Avenida Madero") # 5

medico1 = Medico("Alberto", 1900, "ALB4817BNDDDF", "Av. Periodismo") # 8

hospital.registrar_paciente(paciente=paciente)
hospital.registrar_paciente(paciente=paciente_dos)

hospital.registrar_medico(medico=medico1)

#  Imprimir todo  los pacientes
print("----- Lista de todos los pacientes -----")
hospital.mostrar_pacientes()

# Imprimir pacientes  menores de edad
print("----- Lista  pacientes menores de edad -----")
hospital.mostrar_pacientes_menores_edad()

# Imprimir pacientes mayores de edad
print("----- Lista  pacientes mayores de edad -----")
hospital.mostrar_pacientes_mayores_edad()

# Imprimir todos los medicos
print("----- Lista de todos los médicos -----")
hospital.mostrar_medicos()

# Eliminar un paciente por su ID (usando el ID generado aleatoriamente)
print(f"----- Eliminando paciente con ID {paciente_dos.id} -----")
hospital.eliminar_paciente(paciente_dos.id)

# Mostrar todos los pacientes después de la eliminacion
print("----- Lista de pacientes después de la eliminación -----")
hospital.mostrar_pacientes()

# Eliminar un medico por su ID (usando el ID generado aleatoriamente)
print(f"----- Eliminando médico con ID {medico1.id} -----")
hospital.eliminar_medico(medico1.id)

# Mostrar todos los medicos después de la eliminacion
print("----- Lista de médicos después de la eliminación -----")
hospital.mostrar_medicos()