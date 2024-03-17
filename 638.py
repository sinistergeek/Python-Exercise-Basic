def quad_ac(a,c):
    def f(b,x):
        return quad(a,b,c,x)
    return f

myquad = quad_ac(1,2)
print(myquad(0,1))
print(myquad(1,2))
print(myquad(2,-1))
