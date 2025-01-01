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
