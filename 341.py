filename = __file__
with open(filename)  as fh:
    length = map(len,fh)
    print(length)
    for ln in length:
        print(ln)
