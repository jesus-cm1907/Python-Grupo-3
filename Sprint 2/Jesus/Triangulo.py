class Triangulo():

    def __init__(self, base,altura,lado):
        self.base = base
        self.altura = altura
        self.lado = lado

    def area(self):
        resultado = (self.base*self.altura)/2
        return resultado

    def perimetro(self):
        resultado = self.lado + self.lado + self.lado
        return resultado


t = Triangulo(2, 3, 4)
print('Area triangulo', t.area())
print('Perimetro triangulo', t.perimetro())
