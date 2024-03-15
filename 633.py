def fibonacci():
    c = 0
    n = 1
    while Trie:
        yield c
        c, n = n, c + n 
for i in fibonacci():
    if  i > 100:
        break
