import math

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
        
r = Cuadrado(4,2)
     
print("Area del cuadrado: ", r.area())
print("Perimetro del cuadrado: ", r.perimetro())
