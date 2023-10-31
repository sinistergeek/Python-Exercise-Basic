class Twice_multiply:
    def __init__(self):
        self.calculate(500)
    def calculate(self, num):
        self.num = 2 * num;
class Thrice_multiply(Twice_multiply):
    def __init__(self):
        super().__init__()
        print("num from Thrice_multiply is", self.num)

    def calculate(self, num):
        self.num = 3 * num;
tm = Thrice_multiply()
isinstance(tm,Thrice_multiply)

