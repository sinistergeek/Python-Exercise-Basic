class Summable_List(list):
    def sum(self):
        s = 0
        for v in self:
            s += v
        return s
