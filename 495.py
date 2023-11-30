class Circle:

    def __init__(self,radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,value):
        self._radius = value

circle = Circle(3)
print(circle.__dict__)
