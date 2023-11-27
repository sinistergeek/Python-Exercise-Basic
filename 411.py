from 410 import tron

@tron
def f(a,b=1,*args,**kwargs):
    print('a:',a)
    print('b:',b)
    print('args',args)
    print('kwargs:',kwargs)
    return a+b
f(2,4,5,7,c=8,d=3)
print()
f(2,c=5,d=6)
print()
f(10)
