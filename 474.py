class Laptop:
    def __init__(self,brand,model,price):
        self.brand = brand
        self._model = model
        self.__price = price

laptop = Laptop('Acer','Predator',5490)
print(laptop.__dict__)
