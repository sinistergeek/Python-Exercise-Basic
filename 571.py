# overloading concepts

class work:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        total = self.x + other.x
        total1 = self.y + other.y
        s3 = work(total,total1)
        return s3        
s1 = work(44,33)
s2 = work(33,2)
s3 = s1 + s2
print(s3.x)
print(s3.y)
