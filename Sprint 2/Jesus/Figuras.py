from abc import ABC,abstractmethod
from math import pi 
class Figura(ABC):
    
    @abstractmethod
    def area (self):
        pass
    
    @abstractmethod
    
    def perimetro(self):
            pass
        
class Circulo(Figura):
    
    def __init__(self,radio):
        self.radio=radio
        
    def area(self):
            resultado=pi * self.radio ** 2
            
            return resultado
        
    def perimetro(self):
        resultado =2 * pi* self.radio 
        
        return resultado
        
    
class Rectangulo(Figura):
     def __init__(self,base,alto,lado):
         self.base=base
         self.alto=alto
         self.lado=lado
         
     
     def area(self):
          resultado=self.base * self.alto
          return resultado
      
        
     def perimetro(self):
          resultado= 4* self.lado
          return resultado
        

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

   
 

c =Circulo(5)
print("Calculos del circulo:")
print("Area:", c.area())
print("Perimetro:", c.perimetro())
    
print()
    
    
r=Rectangulo(18,7)
    
print("Calculos del rectangulo:")
print("Area del rectangulo:%.2f" % r.area())
print("Perimetro del rectangulo:%.2f" % r.perimetro())

t = Triangulo(2, 3, 4)
print('Area triangulo', t.area())
print('Perimetro triangulo', t.perimetro())
