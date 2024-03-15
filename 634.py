 def identity(it):
     for x in it:
         yield x

for i in identity(range(4)):
    print(i)
