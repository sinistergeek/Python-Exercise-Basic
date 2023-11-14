dictionary = {'Anna':20,'Mark':15,'Clinton':18,'Alice':10}
names = [*dictionary]
print(names)

arr_of_dicts = [
    {
        'id':num,
        'name':name
    } for num,name in enumerate(names,start=1)

        ]


print(arr_of_dicts)
