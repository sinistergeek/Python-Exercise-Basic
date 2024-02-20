a = ['a',1,2.5,2,'a','my',3,3.5,3.6,2]
b =[]
c =[]
for i in a:
    if (type(i) != int) :
        b.append(i)
    else:
        c.append(i)

print(b)
print(c)

