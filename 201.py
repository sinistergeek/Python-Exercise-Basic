user ={
        'fname' :'Foo',
        'lname' : 'Bar'
        }

for k in user:
    print("{} -> {}".format(k,user[k]))


for k in user.keys():
    user['email'] = 'foo@bar.com'
    print(k)

print('-----')

for k in user:
    user['birthdate'] = '1991'
    print(j)
