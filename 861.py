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
