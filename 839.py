f = open("myfile.txt","r")
print(f.fileno())

collection = [1,2,3,4,5,6,7,8,9,10]
def func(number):
    if number % 2 == 0:
        return True 
    return False 
evenNum = list(filter(func,collection))
print(evenNum)

try:
    value = 100/0
except:
    print("Error Occurs!")
finally:
    print("Remind:Please be careful when you input data!")

str = "JavaScript"
print(str.find("v"))
