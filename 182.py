people  = [{'name' : 'Foo Bar',
            'email' : 'foo@example.com'},
           {
            'name' : 'Qux Bar',
            'email' : 'qux@example.com',
            'children': ['Alpa','Beat']
               }
           ]
print(people)
print(people[0]['name'])
print(people[1]['children'][0])
print(list(map(lambda p: p['name'],people)))
