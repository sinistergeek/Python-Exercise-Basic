def format_person(first,last,age):
    return '{},{} - age{}'.format(last,first,age)
first = ('John','Snne','ary','peter')
last = ('Brown','Smith','Jones','oper')
age = (25,33,41,29)
m = map(format_person,first,last,age)
list(map(print,m))
