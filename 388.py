def sqr(n):
    print(f"sqr {n}")
    return n ** 2

numbers = [1,3,7]
n1 = [sqr(n) for n in numbers]
print("we have the list")
for i in n1:
    print(i)
print("-----")

n2 = (sqr(n) for n in numbers)
print("we have the generator")
for i in n2:
    print(i)
