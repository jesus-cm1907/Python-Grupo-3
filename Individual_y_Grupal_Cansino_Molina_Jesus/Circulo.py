from math import pi

class Circulo:
    
    def __init__(self,radio):
        self.radio=radio
        
    def area(self):
        resultado= pi* self.radio** 2
        return resultado
    
    def perimetro(self):
        resultado = 2 *pi* self.radio
         
        return resultado
    
    
c = Circulo(5)
    
print("Area", c.area())
print("Perimetro:",c.perimetro())
