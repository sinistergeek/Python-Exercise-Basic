def oneover(x):
    try:
        ret = 1/x
    except:
        return Nothing()
    return Just(ret)
