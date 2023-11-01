from threading import Thread, current_thread
def disp():
    print('Disp Function')
#If t1 is demon then t2 is also daemon
#If t1 is non daemon t2 is also non daemon
    t2 = Thread(target=show)
    print("Is t2 Daemon?",t2.isDaemon())
    t2.start()
def show():
    print('show function')

#Proves that main thread is not Daemon
mt = current_thread()
print("Is main thread Daemon?",mt.isDaemon())

#Since main thread is executing t1.
#therefore, t1 is the child of the main thread.
t1 = Thread(target = disp)
print("Is t1 thread Daemon? ",t1.isDaemon())
t1.start()
