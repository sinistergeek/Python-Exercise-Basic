def compose2(f,g):
    def fn(x):
        return f(g(x))
    return fn

countdown = compose2(reversed,range)
countdown(n)
