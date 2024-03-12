def __next__(self):
    if self.pos < len(self.chars):
        c = self.chars[self.pos]
        self.pos += 1
        return c
    else:
        raise StopIteration
