from itertools import chain 
odd = [11,13,15,17,19]
even = [12,14,16,18,20]
num = list(chain(odd,even))
print(num)
