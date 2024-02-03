def not_empty(s):
    if s:
        print('True',s)
        return True

    else:
        print('False')
        return False

k = ['a','','b','']
m = map(same,filter(not_empty,k))
print('Start')
for s in m:
    print('In loop',s)

