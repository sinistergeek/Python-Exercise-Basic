import time 
import threading 
def func():
    time.sleep(2)
    print('myThread is running')
myThread = threading.Thread(target=func)
myThread.start()
print("Is myThread alive?",myThread.is_alive())

str = "year2018";
s = str.isalnum();
print(s)

str = "year2018"
s = str.sisalpha();
print(s)

str = "Hero007"
s = str.isascii()
print(s)

f = open("myFile.txt","r")
print(f.isatty())

str = u"12345678"
s = str.isdecimal();
