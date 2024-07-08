str = "Pandas in 8  Hours"
print(id(str))

x=100
y=200
if y > x:
    print("y is greater than x.")
   
import calendar 
cal = calendar.mont(2020,1)
print(cal)

import os 
os.mkdir("/tmp/home/mydir")

import re 
pattern = re.compile("^(\d{3})-(\d{3})-(\d{4})$")

import smtplib
obj = smtplib.SMPT('localhost')
obj.sendmail(sender,receivers,message.as_string())
