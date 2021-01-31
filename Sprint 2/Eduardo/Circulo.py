from math import pi

class Circulo:
    
    def __init__(self,r):
        self.r=r
    
    def perimetro(self):
        total = 2 *pi* self.r
         
        return total

    def area(self):
        total= pi* self.r** 2
        return total
    
c = Circulo(5)
    
print("Area", c.area())
print("Perimetro:",c.perimetro())