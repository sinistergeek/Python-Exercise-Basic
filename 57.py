from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Figure):
    def __init__(self,a):
        self.a = a

    def area(self):
        return self.a*self.a


try:
    Figure()
except TypeError as error:
    print(error)
