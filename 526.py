def format_person(first,last,age):
    return '{},{} - age {}'.format(last,first,age)
first = ('John','Anne','Mary','Peter')
last = ('Brown','Smith','Jones','Cooper')
age = (25,33,41,28)
m = map(format_person,first,last,age)
list(map(print,m))
