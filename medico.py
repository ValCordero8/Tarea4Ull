import random

class Medico:
    id = 0
    nombre = ""
    ano_nacimiento = 0
    rfc = ""
    direccion = ""

    def __init__(self, nombre, ano_nacimiento, rfc, direccion):
        self.id = random.randint(1, 1000)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.rfc = rfc
        self.direccion = direccion

    def mostrar_informacion(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}, Ano Naciemiento: {self.ano_nacimiento}, rfc: {self.rfc}, Direccion: {self.direccion}")

    # @property
    # def id(self):
    #     return self.id
    
    # @property
    # def name(self):
    #     return self.name
    
    # @property
    # def ano_nacimiento(self):
    #     return self.ano_nacimiento
    
    # @property
    # def rfc(self):
    #     return self.rfc
    
    # @property
    # def direccion(self):
    #     return self.direccion