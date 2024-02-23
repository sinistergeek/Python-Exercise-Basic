print((lambda a,b:a+b)(3,4))
f=lambda a,b:a+b
print(f(3,4))

#recursive lambda expression

g = lambda a:1 if a==0 else a*g(a-1)
print(g(20))
