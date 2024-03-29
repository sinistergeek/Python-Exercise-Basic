import math
s0 = len(data)
s1 = sum(data)
s2 = sum(x ** 2 for x in data)
mean = s1/s0
stdev = math.sqrt(s2/s0 - (s1/s0)**2)
