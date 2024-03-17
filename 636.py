def maxn(n):
    def f(x):
        return max(n,x)
    return f

max0 = maxn(0)
print(max0(3))
print(max0(-1))
