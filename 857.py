def fun1():
    v= "Andy"
    def fun2():
        nonlocal v 
        v = "Rose"
    fun2()
    return v 
print(fun1())
