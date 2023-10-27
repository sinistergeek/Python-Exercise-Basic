x=2

while(x<100):
    y=2
    while(y<=(x/y)):
        if not(x%y):
            break
        y=y+1
        if(y>x/y):
            print(x,"is a prime number.")
        x=x+1

print("Maxium number 100 reached.")
