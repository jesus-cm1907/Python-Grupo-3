from Figura import *    # Importamos todo de la clase padre: Figura


class Cuadrado():

    def __init__(self, lado=0):
        self.lado = lado

# metodo calcular area
    def area(self):
        resultado = lado*lado
        return resultado

# metodo calcular perimetro

    def perimetro(self):
        resultado = lado*4
        return resultado


cu = Cuadrado(2)
print('Area cuadrado: ', cu.area())
print('Perimetro cuadrado: ', cu.area())
