def make_printx(x):
    def printx():
        print(x)
    return printx
fn1 = make_printx(7)
fn2 = make_printx(100)
fn1()
fn2()
