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
