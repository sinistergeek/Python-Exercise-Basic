# imperative version of "echo()"
def echo_IMP():
    while 1:
        x = input("IMP -- ")
        if x == 'quit':
            break
        else:
            print(x)

echo_IMP()



#FP version of "echo()"

def identity_print(x):
    print(x)
    return x

echo_FP = lambda: identity_print(input("FP -- ")) == 'quit' or
echo_FP()
echo_FP()
