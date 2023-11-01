import threading
x=0
y=0

def  thread_sync1(number):
    global x
    global y
    print("thread_sync1 acquiring lock1\n")
    lock1.acquire()
    x=number*2
    print("thread_sync1 acquiring lock2\n")
    if lock2.locked():
        print("in thread_sync1, thre next resource is locked waiting\n")
    else:
        print("We have got the next resource")
        lock2.acquire()
        z = x+y
        print("z =",z)
        print("thread_sync1 releasing lock2\n")
        lock2.release()
        print("thread_sync1 releaseing lock1\n")
        lock1.release()
        print("thread_sync1 done\n")
def thread_sync2(number):
    global x
    global y
    print("thread_sync2 acquiring lock2\n")
    lock2.acquire()
    y = number*4
    print("thread_synce2 acquiring lock1\n")
    if lock1.locked():
        print("in thread_sync2, the next resouce is locked waiting\n")
    else:
        print("We have got the next resouce")
        lock1.acquire()
        v = y - x
        print("v = ",v)
        print("thread_sync2 releasing lock1\n")
        lock1.release()
        print("thread_sync2 releasing lock2\n")
        lock2.release()
        print("thread_sync2 done\n")
lock1 = threading.Lock()
lock2 = threading.Lock()
t1 = threading.Thread(target = thread_sync1, args =(2,))
t2 = threading.Thread(target = thread_sync2, args =(3,))
t1.start()
t2.start()
t1.join()
t2.join()

