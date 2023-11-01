import threading
import time

def print_if_daemon():
    print("inside target function")
    if t1.isDaemon():
        print(threading.currentThread().name,"is a daemon!!")

t1 = threading.Thread(target = print_if_daemon)
#Check if t1 is daemon thread
print("Present Status of thread t1 is: ",t1.isDaemon())

#Set t1 as Deamon thread
t1.setDaemon(True)

#start()
t1.start()

time.sleep(5)
print("Main Exiting")
t1.join()
