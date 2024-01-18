def flatten(x):
    if not isinstance(x,list):
        return [x]
    if x == []:
        return x
    r = []
    for e in x:
        if isinstance(e,list):
            r += flatten(e)

        else:
            r.append(e)

    return r

