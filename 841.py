f = open("myfile.txt","a")
f.write("Hello World!")
f.flush()
print("The buffer has been cleared!")

for str in 'Good': 
    print(str)

myTuple = ("apple","banana","cherry")
for elements in myTuple:
    print(elements)


for num in range(3,10):
    print(num)
