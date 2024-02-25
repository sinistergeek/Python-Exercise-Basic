v = (1,0,2,0,5)
u = []
for x in v:
    u.append(x)
    if x == 0:
        u.append(x)
t = tuple(u)
print(t)
