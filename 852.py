str = "VERY GOOD"
s = str.isupper();
print(s)

student = {
    "name":"Andy",
    "id":"0026"
}
print(student.items())

iterator = iter(["ant","bee","cat"])
print(next[iterator])
print(next[iterator])
print(next[iterator])

separator ="-";
str = ("x","y","z");
print(separator.join(str));


from time import sleep 
from threadiang import thread 
def fun():
    sleep(2)
    print('Joined thread finished running.')

thread = Thread(target=fun)
thread.start()
print('Main thread is waiting for joined thread to terminate.')
thread.join()
print('Main thread resumes running after joined thread terminates.')
