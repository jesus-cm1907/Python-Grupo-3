from abc import ABC, abstractmethod


class Figura():
    # definimos metodo area como abstracto
    @abstractmethod
    def area(self):
        pass

    # definimos metodo perimetro como abstracto
    @abstractmethod
    def perimetro(self):
        pass
