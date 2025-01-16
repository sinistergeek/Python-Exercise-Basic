def get_speak_func(text,volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell 
    else:
        return whisper 

get_speak_func('Hello,World',0.7)()

add = lambda x,y: x + y
add(5,3)

def make_adder(n):
    return lambda x: x + n 

plus_3 =make_adder(3) 
plus_5 =make_adder(5) 
plus_3(4)
plus_5(4)

class Car:
    rev = lambda self:print('Wroom!')
    crash = lambda self:print('Boom!')
my_car = Car()
my_car.crash()

@null_decorator
def greet():
    return 'Hello!'
greet()

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result 
    return wrapper


def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

musician = get_formatted_name('jimi','hendrix')
print(musician)
musician =get_formatted_name('john','hooker','lee')
