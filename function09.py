your_age = lambda yr_of_birth:2023 - yr_of_birth
print(your_age(1956))



numbers = [1,2,3,4,5,6,7,8,9]
odd_number = list(filter(lambda x : (x%2!=0), numbers))
print(odd_number)

list1 = [1,2,3,4,5]
print(list(map(lambda x: x**2,list1)))
