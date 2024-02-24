def decor_me(test_me):
    def distinction(passet):
        for n in passet:
            if n > 45:
                print('Dinsiontion')
        else:
            test_me(passet)
    return distinction
@decor_me
def tes(passet):
    for m in passet:
        if m > 33:
            print('Pass',m)
        else:
            print('Fail',m)
            break
    else:
        print('Result: Pass')

tes([45,45,66,77,44])
