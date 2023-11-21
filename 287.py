class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({},{})".format(self.x,self.y)

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

class Polygon:
    def __init__(self,*args):
        self.points = args

    def __repr__(self):
        return 'Polygon('+ ', '.join(map(lambda p: str(p),self.points)) + ')'

    def move(self,dx,dy):
        for p in self.points:
            p.move(dx,dy)

p1 = Point(0,0)
p2 = Point(5,7)
p3 = Point(4,9)

print(p1)
print(p2)
print(p3)

p1.move(2,3)
print(p1)

poly = Polygon(p1,p2,p3)
print(poly)
poly.move(-1,1)
print(poly)
