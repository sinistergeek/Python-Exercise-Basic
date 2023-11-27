from warnings import warn

def foo():
    warn("Foo will deprecate soon.Use bar() instead",DeprecationWarning)
    print("Foo still works")


def main():
    foo()
    print("afterfoo")

main()
