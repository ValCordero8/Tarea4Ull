class Maestro:
    nombre: str
    apellido: str
    rfc: str
    sueldo: float
    numero_control_maestro: str
    
    def __init__(self,nombre: str, apellido: str, rfc: str, sueldo: float, numero_control_maestro):
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo
        self.numero_control_maestro = numero_control_maestro


    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"  
        info = f"RFC: {self.rfc}, Nombre Completo: {nombre_completo}, Sueldo: {self.sueldo}, ID: {self.numero_control_maestro}"
        return info