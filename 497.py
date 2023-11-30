import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,value):
        self._radius = value
        self._area = None
        self._preimeter = None

    @property
    def area(self):
        if self.area is None:
            self._area = math.pi * self._radius*self._radius
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self.permiter = 2 * math.pi * self._radius
        return self._perimter
circle = Circle(3)
print(f'{circle.permiter:.4f}')
