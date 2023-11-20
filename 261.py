import subprocess
import sys

command = [sys.executable,'1.py']

proc = subprocess.Popen(command,stdout=subprocess.PIPE,stderr = subprocess.PIPE)

out,err = proc.communicate()
print('exit code:',proc.returncode)

print('out:')
for line in out.decode('utf8').split('\n'):
    print(line)
print('err:')
for line in err.decode('utf8').split('\n'):
    print(line)
