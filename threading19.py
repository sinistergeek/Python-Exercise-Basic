import threading
def thread_count(count):
    print("I am the thread number",count,".")
    print("My name is ", threading.currentThread().getName())
    print("active count",threading.activeCount())
    l1 = threading.enumerate()
    for i in l1:
        print(i)

for i in range(1,3):
    t = threading.Thread(target = thread_count,args = (i,))
    t.start()
    t.join()
