
from usuario.usuario import Usuario  

class Coordinador(Usuario):
    def __init__(self, nombre, sueldo, rfc, anos_antiguedad):
        super().__init__(nombre)  
        self.sueldo = sueldo
        self.rfc = rfc
        self.anos_antiguedad = anos_antiguedad

    def __str__(self):
        return f"Coordinador: {self.nombre}, Sueldo: {self.sueldo}, RFC: {self.rfc}, Años de Antigüedad: {self.anos_antiguedad}"
