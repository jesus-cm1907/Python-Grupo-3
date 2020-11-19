from abc import ABC, abstractmethod


class Figura():
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass
