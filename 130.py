def get_name(dictionary: dict) -> str:
    return dictionary.get('name','Unknown name')

arr = [
    {
        'name':'john',
        'age':25
    },
    {
        'age':20
    },
    {
        'name':'Tom',
        'age' : 38
    },
    {}
        ]
for dictionary in arr:
    print(get_name(dictionary))
