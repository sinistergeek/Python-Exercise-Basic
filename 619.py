def f(x,a,v):
    def g(e):
        print(x,a,v,e)
    return g
c = f(5,6,7)
