from Figura import *    # Importamos todo de la clase padre: Figura


class Circulo():
    pi = 3.1416

    def __init__(self, r=0):
        self.r = r

# metodo calcular area
    def area(self):
        resultado = self.r * self.r * Circulo.pi
        return resultado

# metodo calcular perimetro

    def perimetro(self):
        resultado = 2 * (Circulo.pi) * r
        return resultado
    
# metodo calcular diametro
    def diametro(self):
        resultado = 2 * r
        return resultado


ci = Circulo(2)
print('Area circulo: ', ci.area())
print('Perimetro circulo: ', ci.perimetro())
print('Diametro circulo: ', ci.diametro())
