import math

class Circulo:
    # Constructor para inicializar  con el radio
    def __init__(self, radio):
        self.radio = radio

    # Metodo para calcular el area 
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    # Metodo para calcular el perimetro 
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio