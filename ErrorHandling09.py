def just_having_fun():
    try:
        print(4)
    except TypeError as e:
        print(str(e))
    finally:
        print("Ok Bye")
just_having_fun()
