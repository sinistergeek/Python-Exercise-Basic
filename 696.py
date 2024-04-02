def compose(*funcs):
    def inner(data, funcs=funcs):
        result = data
        for f in reversed(funcs):
            result = f(result)
        return result
    return inner

times2 = lambda x: x*2
minus3 = lambda x: x-3
mod6 = lambda x: x%6
f = compose(mode6,times2,minus)
all(f(i)==((i-3)*2)%6 for i in range(100000))

