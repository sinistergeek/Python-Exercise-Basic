import time,sys

for i in range(10):
    sys.stdout.write('\r' + '=' * i)
    sys.stdout.flush()
    time.sleep(1)
