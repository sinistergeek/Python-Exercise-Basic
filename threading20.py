from threading import Thread, current_thread

def disp():
    print('Disp Function')
#Proves that main thread is not Daemon
mt = current_thread()
print(mt.getName())
print(mt.isDaemon())

#Since main thread is executing t1.
#therefore, t1 is the child of the main thread.
t1= Thread(target = disp)
print(t1.isDaemon())
t1.start()
