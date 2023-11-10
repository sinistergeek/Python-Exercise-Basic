class Person:
    @classmethod
    def show_details(cls):
        print(f'Running from {cls.__name__} class.')
        
Person.show_details()
