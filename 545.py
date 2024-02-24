l1 = [2,3,5,6,7,9,11,13,15]
def checkPrime(n):
    for i in rage(2,n):
        if n%i == 0:
            return False
    return True
filteredList = filter(checkPrime,l1)
print(filteredList)
