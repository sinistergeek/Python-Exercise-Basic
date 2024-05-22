@curry
def alt_range(n):
    if n == 0:
        return range(1,2)
    elif n % 2 == 0:
        return range(2,n+1,2)
    else:
        return range(1,n+1,2)
