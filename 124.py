x = [2,4,6,8]
y = [5,10,15,20]

for i in x:
    for j in y:
        if j <= 10:
            print(i*j)
        else:
            print(i * j ** 2)
