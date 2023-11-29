class Laptop:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price


    def display_instance_attrs(self):
        for attr in self.__dict__.keys():
            print(attr)


laptop = Laptop('Dell','Inspiron',3559)
laptop.display_instance_attrs()
