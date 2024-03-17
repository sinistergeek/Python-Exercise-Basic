def make_print(sep):
    def f(*args):
        return print(*args,sep=sep)
    return f

print_csv = make_print(', ')
print_colon = make_print(':')
print_csv(1,2,3)
print_colon(1,2,3)
