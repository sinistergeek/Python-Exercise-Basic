def convert(f,x):
    y = f(x)
    print(x,'=>',y)


def c2f(x):
    return x*1.8 + 32

convert(c2f,18)


def i2text(x):
    text = ['zero','one','two','three']
    return text[x]

convert(i2text,2)
