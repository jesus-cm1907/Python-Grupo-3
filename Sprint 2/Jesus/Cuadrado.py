class Rectangulo:
    
    def __init__(self,alto,base,lado):
      
      self.alto=alto
      self.base=base
      self.lado=lado
      
      
    def area(self):
          resultado =self.base * self.alto
          
          return resultado
      
        
    def perimetro(self):
         resultado= 4* self.lado
         
         return resultado
     
        
r = Rectangulo(18,7,6)
     
print("Area del rectangulo:%.2f" % r.area())
print("Perimetro del rectangulo: %.2f" % r.perimetro())

  
    