import math

class Triangulo():

    def __init__(self, b,h,l):
        self.b = b
        self.h = h
        self.l = l

    def area(self):
        total = (self.b*self.h)/2
        return total

    def perimetro(self):
        total = self.l + self.l + self.l
        return total


t = Triangulo(3, 2, 4)

print('Area triangulo', t.area())
print('Perimetro triangulo', t.perimetro())