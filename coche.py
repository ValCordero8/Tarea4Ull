class Coche:
        marca = ""
        año = 0
        modelo = ""

        def __init__(self, marca, modelo, año):
                    self.marca = marca
                    self.modelo = modelo
                    self.año = año
     #Metodo
        
        def mostrar_informacion(self):
         print("Marca", self.marca)
         print("Modelo", self.modelo)
         print("Año", self.año)    

        
          