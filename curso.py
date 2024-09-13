

class Curso:
    def __init__(self, nombre_curso, codigo_curso, instructor):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.instructor = instructor

    def mostrar_info_curso(self):
        print(f"Curso: {self.nombre_curso}, Código: {self.codigo_curso}, Instructor: {self.instructor}")
