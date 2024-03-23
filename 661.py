def within(e,iterable):
    def head_tail(e,a,iterable):
        b = next(iterable)
        if abs(a-b) <= e:return b
        return head_tail(e,b,iterable)
    return head_tail(e,next(iterable),iterable)
