name_for_userid = {
        382: 'Alice',
        950: 'Bob',
        590: 'Dilbert',

        }

def greeting(userid):
    return 'Hi %s!' %s name_for_userid[userid]

greeting(382)
greeting(33333)

def greeting(userid):
    if userid in name_for_userid:
        return 'Hi %s!' % name_for_userid[userid]
    else:
        return 'Hi there!'

greeting(382)
greeting(333)

def greeting(userid):
    try:
        return 'Hi %s!' % name_fro_userid[userid]
    except KeyError:
        return 'Hi there'

import operator
sorted(xs.items(),key=operator.itemgetter(1))
sorted(xs.items(),
       key=lambda x: x[1],
       reverse=True)
if cond == 'cond_a':
    handle_a()
elif cond == 'cond_b':
    handle_b()
else:
    handle_default()

def myfunc(a,b):
    return a + b
funcs = [myfunc]
print(funcs[0])

func_dict={
        'cond_a': handle_a,
        'cond_b': hand;e_b
        }
cond = 'cond_a'
print(func_dict[cond]())

def dispatch_if(operator,x,y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y

def dispatch_dict(operator,x,Y):
    return{
        'add': lambda: x + Y,
        'sub': lambda: x - Y,
        'mul': lambda: x * Y,
        'div': lambda: x / Y.
        }.get(operator,lambda:None)()


class AlwaysEquals:
    def __eq__(self,other):
        return True
    def __hash__(self):
        return id(self)

AlwaysEquals()

objects = [
AlwaysEquals(),
AlwaysEquals(),
AlwaysEquals()
        ]
[hash(obj) for obj in objects]

class SameHash:
    def __hash__(self):
        return 1 


xs = {'a':1,'b':2}
ys = {'b':3,'c'4}
zs = {}
zs.update(xs)
zs.update(ys)

def update(dict1,dict2):
    for key, value in dict2.items():
        dict[key] = value
print(zs)

mapping = {'a': 23, 'b':42,'c':0xc0ffee}
str(mapping)

import json
json.dumps(mapping,indent=4,sort_keys=True)

import pprint
pprint.pprint(mapping)

import datetime
print(dir(datetime))
[ _ for _ in dir(datetime) if 'date' in _.lower()]

def greet(name):
    return 'Hello, ' + name + '!'
print(greet('Guido'))

name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())
