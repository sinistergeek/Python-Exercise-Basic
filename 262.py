import subprocess
import sys
import time

proc = subprocess.Popen([sys.executable,'03.py'], stdout = subprocess.PIPE,stderr = subprocess.PIPE)

timeout = 6
while True:
    poll = proc.poll()
    print(poll)
    time.sleep(0.5)
    time -= 0.5
    if timeout <= 0:
        break
    if poll is not None:
        break
print("Final: {}".format(poll))
if poll is None:
    pass
else:
    out,err = proc.communicate()
    print(out)
    print(err)
