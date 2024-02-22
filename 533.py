c = int(input("Enter the number"))
d3 = {}

for i in range(c):
    keey = int(input('Enter the key'))
    d = input("the value")
    d3[keey] = d

print(d3)
new =d3

for q,r in new.items():
    if q == r :
        print('value == key')
    if q != r :
        print(q,r)

