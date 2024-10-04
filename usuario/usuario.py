from .utilidades.roles import Rol

class Usuario:
    numero_control: str
    nombre: str
    apellido: str 
    contrasenia: str
    rol: str  

    def __init__(self, numero_control: str, nombre: str, apellido: str, contrasenia: str, rol: Rol):
        self.numero_control= numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol 
        self.contrasenia = contrasenia

    def metodo():
        pass 
 

