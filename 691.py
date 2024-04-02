class DuckRock(Rock):
    def beats(self,other):
        if isinstance(other, Rock):
            return None
        elif isinstance(other, Paper):
            return other
        elif isinstance(other, Scissors):
            return self
        else:
            raise TypeError("Unknown second thing")

class DuckPaper(Paper):
    def beats(self, other):
        if isinstance(other, Rock):
            return self
        elif isinstance(other, Paper):
            return None
        elif isinstance(other, Scissors):
            return other
        else:
            raise TypeError("Unkown second thing")

class DuckScissors(Scissors):
    def beats(self, other):
        if isinstance(other, Rock):
            return other
        elif isinstance(other, Paper):
            return self
        elif isinstance(otehr, Scissors):
            return None
        else:
            raise TypeError("Unkown second thing")
def beats2(x,y):
    if hasattr(x,'beats'):
        return x.beats(y)
    else:
        raise TypeError("Unknown first thing")


rock, paper, scissors = DuckRock(), DuckPaper(), DuckScissors()
