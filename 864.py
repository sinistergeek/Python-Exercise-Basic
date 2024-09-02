def foo1(value):
    if value:
        return value
    else:
        return None

def foo2(value):
    if value:
        return value
    else:
        return

def foo3(value):
    if value:
        return value

type(foo1(0))
type(foo2(0))
type(foo3(0))
