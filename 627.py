def sumcount(it):
    sum = 0
    count = 0
    for x in it:
        sum += x
        count += 1
    return sum, count
s = filter(lambda x : x not in ('a', 'the'),strings)
total,count = sumcount(map(len,s))
average = total/count
