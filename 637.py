def quad(a,b,c,x):
    return a*x*x + b*x + c

def quad_abc(a,b,c):
    def f(x):
        return quad(a,b,c,x)
    return f
