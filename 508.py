def func(*args,**kwargs):
    print(args)
    print(kwargs)

data = {'x':1,'y':2,'z':3}
data2 = [12,33,'s','p']
func(*data2,**data)



