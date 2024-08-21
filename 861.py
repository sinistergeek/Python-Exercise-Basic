from string import Template 
t = Template('Hey, $name!')
t.substitute(name=name)

templ_string = 'Hey $name, there is a $error error!'
Template(templ_string).substitute(name=name,error=hex(errno))

SECRET = 'this-is-a-secret'
class Error:
    def __init__(self):
        pass 

err = Error()
user_input = '{error.__init__.__globals__[SECRET]}'
user_input.format(error=err)

def yell(text):
    return text.upper() + '!'
yell('hello')

def greet(func):
    greeting = func('Hi,I am a Python program')
    print(greeting)
greet(bark)

def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text) 
speak('Hello, World')

def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell 
    else:
        return whisper 

get_speak_func(0.3)
get_speak_func(0.7)
