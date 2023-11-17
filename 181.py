a = {"foo":"two","Two":"luuu","pooh":"Who"}

for k in a.items():
    print(k)

for j in a.keys():
    print(j)

for  name,id in a.items():
    print("{} == {}".format(name,id))
