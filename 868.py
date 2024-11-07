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
