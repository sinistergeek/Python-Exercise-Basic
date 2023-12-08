def greet(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')

greet(name = 'Edcorner',greeting='Hello')
greet(name = 'Jane',greeting='Hi',age=30)
