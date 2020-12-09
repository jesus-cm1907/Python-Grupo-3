from Figura import *


class Triangulo():

    def __init__(self, b=0, h=0, lado=0):
        self.b = b
        self.h = h
        self.lado = lado

    def area(self):
        resultado = (b*h)/2
        return resultado

    def perimetro(self):
        resultado = lado + lado + lado
        return resultado


t = Triangulo(2, 3, 4)
print('Area triangulo', t.area())
print('Perimetro triangulo', t.perimetro())
