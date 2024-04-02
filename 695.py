from collections.abc import Iterable
class Fibonacci(Iterable):
    def __init__(self):
        self.a,self.b = 0, 1
        self.total = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b, self.a + self.b
        self.total += self.a
        return self.a
    def running_sum(self):
        return self.total
