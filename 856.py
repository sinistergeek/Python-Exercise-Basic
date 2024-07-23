str = "Hello Hey!"
mytable = str.maketrans("e","a")
print(str.translate(mytable))

def mul(n):
    return n*10
p = [1,2,3]
print(list(map(mul,p)))
