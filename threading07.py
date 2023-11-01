import threading
x = 0
range_val = int(input("Enter the range : "))
def thread_sync():
    global x
    for i in range(range_val):
        x += 1
t1 = threading.Thread(target = thread_sync)
t2 = threading.Thread(target = thread_sync)
t1.start()
t2.start()
t1.join()
t2.join()
print(x)
