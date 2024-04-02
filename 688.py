import math
class RightTriangle(object):
    @staticmethod
    def hypotenuse(a,b):
        return math.sqrt(a**2 + b**2)
    @staticmethod
    def sin(a,b):
        return a / RightTriangle.hypotenuse(a, b)

    @staticmethod
    def cos(a,b):
        return b / RightTriangle.hypotenuse(a,b)
