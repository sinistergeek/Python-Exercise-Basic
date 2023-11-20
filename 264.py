import time
print(time.time())

print(time.timezone)
print(time.daylight)

print(time.gmtime())

t = time.gmtime()
print(t.tm_year)
print(time.strftime('%Y-%m-%d %H:%M:%S'))
