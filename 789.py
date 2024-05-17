class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add_coordinate(self,others):
        new_x = self.x + others.x 
        new_y = self.y + others.y 

c1 = Coordinate(5,6)
c2 = Coordinate(7,9)

c3 = Coordinate(c1.x + c2.x,c1.y + c2.y)
print(c3.x)
print(c3.y)
