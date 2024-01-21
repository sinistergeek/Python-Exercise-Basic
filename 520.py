class Format():
    def __init__(self):
        self.p = 0
        self.w = 0

    def prec(self,n):
        self.p = n
        return self
    def width(self,n):
        self.w = n
        return self
    def __call__(self,x):
        return '{:{width}.{prec}f}'.format(x,width=self.w,prec=self.p)

format3 = Format().width(10).prec(3)
print(format3(1.2345678))
