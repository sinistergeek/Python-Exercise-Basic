favorite_languages ={
        'jen': 'python',
        'sarah' : 'c',
        'edward':'rust',
        'phil': 'python',
        }
for name,language in favorite_languages,items():
    print(f"{name.title()}'s favorite language is {language.little()}.")


friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}!")

aliens = []

for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")

print(f"Total number of aliens: {len(aliens)}")

favorite_languages = {
'jen':['python','rust'],
'sarah': ['c'],
'edward':['rust','go'],
'phil':['python','haskell'],
        }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

users = {

        'aeinstein':{
            'first':'albert',
            'last': 'einstein',
            'location': 'princeton',
            },
        'mcurie':{
            'first':'marie',
            'last' : 'curie',
            'localtion':'paris',
            },

        }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\t Full name: {full_name.title()}")
    print(f"\t Location: {location.title()}")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\n You'll be able to ride when you're a little older.")


number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\n The number {number} is even.")
else:
    print(f"\n The number {number} is odd.")

current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

unconfirmed_users = ['alice','brain','candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\n The following users have been confirmed.")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}
polling_active = True
while polling_active:
    name = input("\n What is your name?")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes / no)")
    if repeat == 'no':
        polling_active =False

print("\n --- Poll Results ---")
for name,response in responses.items():
    print(f"{name} should like to climb {response}.")

def greet_user(username):
    print(f"Hello, {username.title()}!")
greet_user('jesse')

def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
def build_person(first_name,last_name,age=None):
    if age:
        person['age'] = age

musician = build_person('jimi','hendrix',age=27)

while True:
    prin("\nPlease tell me ur name.")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\n Hello,{formatted_name}!")
