from Figura import *


class Cuadrado():

    def __init__(self, lado=0):
        self.lado = lado

    def area(self):
        resultado = lado*lado
        return resultado

    def perimetro(self):
        resultado = lado*4
        return resultado


cu = Cuadrado(2)
print('Area cuadrado: ', cu.area())
print('Perimetro cuadrado: ', cu.area())
