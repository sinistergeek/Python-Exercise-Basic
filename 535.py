def inch2cm(x):
    return x*2.54
def convert(f,x):
    y = f(x)
    print(x, '=>',y)

convert(inch2cm,3)
