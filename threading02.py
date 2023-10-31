import threading
def thread_count(count):
    print("I am the thread number ",count,".")
    print("My name is",threading.current_thread().getName())

for i in range(1,6):
    t = threading.Thread(target = thread_count, args = (i,))
    t.start()
    t.join()
