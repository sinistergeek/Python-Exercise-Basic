class Fibonacci:
    def __init__(self,limit=0):
        self.values = []
        self.limit = limit
    def __iter__(self):
        return self
    def next(self):
        if self.limit and len(self.values) >= self.limit:
            raise StopIteration
        if len(self.values) == 0:
            self.values.append(1)
            return 1
        if len(self.values) == 1:
            self.values.append(1)
            return 1
        self.values.append(self.values[-1] + self.values[-2])
        return self.values[-1]
