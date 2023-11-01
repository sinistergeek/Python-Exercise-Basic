import threading
import time
#The function task(), takes event object and time as aparameter
def task(event, sec):
    print("Started thread but waiting for event...")
    #make the thread wait for event with timeout set
    internal_set = event.wait(sec)
    if internal_set:
        print("Event set")
    else:
        print("Time out, event not set")
#initializing the vent object
e=threading.Event()
#starting the thread, target function is task, name = Event-Blocking-Thead,
#passes an event object and time of 5 seconds
t1 = threading.Thread(name='Event-blocking-Thread',target=task, args=(e,5))
t1.start()
#Letting the main thread sleep for 3 seconds
time.sleep(3)

