class Laptop:
    def __init__(self,price):
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError('The price attriute must be an oint or float type.')
        if not value > 0:
            raise ValueError('The price attribute must be positive int or float value.')
        self._price = value

try:
    laptop = Laptop(-3488)
except ValueError as error:
    print(error)
