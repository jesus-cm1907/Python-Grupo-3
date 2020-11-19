from Figura import *


class Circulo():
    pi = 3.1416

    def __init__(self, r=0):
        self.r = r

    def area(self):
        resultado = self.r * self.r * Circulo.pi
        return resultado

    def perimetro(self):
        resultado = 2 * (Circulo.pi) * r
        return resultado

    def diametro(self):
        resultado = 2 * r
        return resultado


ci = Circulo(2)
print('Area circulo: ', ci.area())
print('Perimetro circulo: ', ci.perimetro())
print('Diametro circulo: ', ci.diametro())
