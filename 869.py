motorcycles= ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

first_owned = motorcycles.pop(0)
print(f"The first  motorcycle I owned was a first_owned.title()}.")

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.reverse()
print(cars)

magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
print(f"I can't wait to see your next trick, {magician,title()}.\n")

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)

print("\n My friend's favorite foods are:")
print(friend_foods)
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

dimensions = (500,50)
print(dimensions[0])
print(dimensions[1])
