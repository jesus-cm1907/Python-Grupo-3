from abc import ABC,abstractmethod
from math import pi 
class Figura(ABC):
    
    @abstractmethod
    def area (self):
        pass
    
    @abstractmethod
    
    def perimetro(self):
            pass
        
class Circulo:
    
    def __init__(self,r):
        self.r=r
    
    def perimetro(self):
        total = 2 *pi* self.r
         
        return total

    def area(self):
        total= pi* self.r** 2
        return total
        
    
class Cuadrado:
    
    def __init__(self,h,b,l):
      
      self.h=h
      self.b=b
      self.l=l
      
        
    def perimetro(self):
         total= 4* self.l
         
         return total
       
    def area(self):
          total =self.b * self.h
          
          return total  
        

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


c =Circulo(2)

print("Calculos del circulo:")
print("Area:", c.area())
print("Perimetro:", c.perimetro())    
    
r=Cuadrado(4,2)
    
print("Calculos del rectangulo:")
print("Area del rectangulo:%.2f" % r.area())
print("Perimetro del rectangulo:%.2f" % r.perimetro())

t = Triangulo(3,2,4)

print('Area triangulo', t.area())
print('Perimetro triangulo', t.perimetro())
