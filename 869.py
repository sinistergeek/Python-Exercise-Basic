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

dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())


requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish.")


age = 19
if age >=18:
    print("You are old enough to vote!")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $20.")
else:
    print("Your admission cost is $40.")

requested_toppings = ['mushrooms','extra cheese']
if 'mushtrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\n Finished making your pizza!")

alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

del alien_0['points']
print(alien_0)

user_0 = {
        'username':'efermi',
        'first' : 'enrico',
        'last' : 'fermi',
        }
for key,value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms','extra cheese'],
        }
print(f"You orderd a {pizza['crust']}- crust pizza" 
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

prompt = "\nPlease enter the the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quite':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

x = 1 
while x <= 5:
    print(x)
    x += 1

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hananah','ty','margot']
greet_users(usernames)

my_dog = Dog('Willie',6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

def update(self):
    """Move the bullet up the screen."""
    #Update the exact position of the bullet.
    self.y -= self.settings.bullet_speed
    #Update the rect position.
    self.rect.y = self.y

def draw_bullet(self):
    """Draw the bullet to the screen."""
    pygame.draw.rect(self.screen,self.color,self.rect)
