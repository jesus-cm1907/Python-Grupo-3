from Figura import *    # Importamos todo de la clase padre: Figura


class Triangulo():

    def __init__(self, b=0, h=0, lado=0):
        self.b = b
        self.h = h
        self.lado = lado

# metodo calcular area
    def area(self):
        resultado = (b*h)/2
        return resultado
    
# metodo calcular perimetro
    def perimetro(self):
        resultado = lado + lado + lado
        return resultado


t = Triangulo(2, 3, 4)
print('Area triangulo', t.area())
print('Perimetro triangulo', t.perimetro())
