def shopping(**kwargs):
    print(kwargs)
    if kwargs:
        print('you bought',kwargs['dress'])
        print('you bought',kwargs['food'])
        print('you bought',kwargs['Shampoo'])
shopping(dress = 'test', Shampoo='Dove', food='Pedigree Puppy')
