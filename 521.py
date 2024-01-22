class Alphabet():
    chars = 'abcde'
    def __init__(self):
        self.pos = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.pos < len(self.chars):
            c = self.chars[self.pos]
            self.pos += 1
            return c
        else:
            raise StopIteration
for c in Alphabet():
    print(c)
