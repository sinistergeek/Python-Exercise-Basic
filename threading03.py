import time
names=[]
def getnames():
    guest_name = input("Enter a guest name")
    names.append(guest_name)
    confirmation = input("Any more guests? (y/n) : ")
    if(confirmation == 'y'):
        getnames()

def welcome_guests(names):
    for name in names:
        print("Wellcome to our club",name)
        time.sleep(5)

def get_id(names):
    count =1
    for name in names:
        print("The guest_id of ",name,"is :",count)
        count = count+1
        time.sleep(10)

getnames()
welcome_guests(names)
get_id(names)
