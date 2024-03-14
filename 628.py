import functools
def opsumcount(a,b):
    return(b[0],a[1] + b[1])

s = filter(lambda x : x not in ('a','the'), strings)
m = map(len,s)
length,total = functools.reduce(opsumcount,enumerate(m,1))
average = total/length
print(average)
