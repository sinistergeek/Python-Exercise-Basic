str = "Hello Hey!"
mytable = str.maketrans("e","a")
print(str.translate(mytable))

def mul(n):
    return n*10
p = [1,2,3]
print(list(map(mul,p)))

import re 
pattern = re.compile("^(\d{3})-(\d{3})-(\d{4})$")

import math 
parameter 
print(math.copysign(10,-10))
print(math.copysign(-20,20))

import math 
print(math.fabs(-3.14))
print(math.fabs(-100))

import math 
print(math.factorial(5))
print(math.factorial(6))

import math 
print(math.floor(9.5))

import math 
print(math.isnan(100))
print(math.isnan(math.nan))

import math 
print(math.isqrt(10))
print(math.isqrt(17))

import math 
lcm = 3/math.gcd(3,4)*4 
print(lcm)

def bounded_repeater(value,max_repeats):
    for i in range(max_requests):
        yield value

iterator = bounded_repeater('Hello',3)
