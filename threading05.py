import time
import threading
class learning_subclassing(threading.Thread):
    def run(self):
        print('\n thread {} has started'.format(self.getName()), "\n")
        try:
            if self._target:
                self._target(*self._args,**self._kwargs)
        finally:
            del self._target, self._args, self._kwargs

def nap(sec,name):
    print("\n Hi I am a thread and my name is {}. I am here only to take a nap of {} seconds".format(name,sec),"\n")
    time.sleep(sec)
    print("{} seconds are over {} is up!!".format(sec,name),"\n")

t1 = learning_subclassing(target = nap, name = "King-thread",args = (10,"King-thread",))
t2 = learning_subclassing(target = nap, name = "Queen-thread",args = (6,"Queeen-thread"))
t3 = learning_subclassing(target = nap, name = "Page-thread",args = (7,"Page-thread"))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
