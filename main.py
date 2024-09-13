

from estudiante import Estudiante
from curso import Curso

# Crear cursos
curso1 = Curso("Matemáticas", "MAT88", "Juan Tinoco")
curso2 = Curso("Historia", "HIS89", "Karla Gomez")
curso3 = Curso("Biología", "BIO90", "Luis Lopez")

# Crear estudiantes
estudiante1 = Estudiante("Valeria", 20, "E1")
estudiante2 = Estudiante("Oscar", 22, "E2")

# Asignar cursos a los estudiantes
estudiante1.agregar_curso(curso1)
estudiante1.agregar_curso(curso2)

estudiante2.agregar_curso(curso2)
estudiante2.agregar_curso(curso3)

# Mostrar la info de los estudiantes
print("Información de los estudiantes:")
estudiante1.mostrar_informacion()
estudiante2.mostrar_informacion()
