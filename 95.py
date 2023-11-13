def my_func(x, **kwargs):
    return x * sorted(kwargs.values())[-1]

result = my_func(10,val1=10,val2=15,val3=20,val4=25,val5=30)
print(result)
