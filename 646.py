from oslash import Just, Nothing

def oneover(x):
    ret = 1/x
    return Just(ret)


a = Just(2).bind(oneover)
print(a)
a = Just(0).bind(oneover)
print(a)
