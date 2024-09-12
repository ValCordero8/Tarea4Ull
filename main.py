from circulos import Circulo

# Crear tres circulos con r diferente
circulo1 = Circulo(3)
circulo2 = Circulo(5)
circulo3 = Circulo(7)

# Imprimir el area y perímetro de cada círculo
print(f"Círculo 1 - Radio: {circulo1.radio}, Área: {circulo1.calcular_area():.2f}, Perímetro: {circulo1.calcular_perimetro():.2f}")
print(f"Círculo 2 - Radio: {circulo2.radio}, Área: {circulo2.calcular_area():.2f}, Perímetro: {circulo2.calcular_perimetro():.2f}")
print(f"Círculo 3 - Radio: {circulo3.radio}, Área: {circulo3.calcular_area():.2f}, Perímetro: {circulo3.calcular_perimetro():.2f}")