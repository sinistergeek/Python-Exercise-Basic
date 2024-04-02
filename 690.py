def beats(x,y):
    if isinstance(x,Rock):
        if isinstance(y,Rock):
            return None
        elif isinstance(y,paper):
            return y
        elif isinstance(y, Scissors):
            return x
        else:
            raise TypeError("Unkown second thing")
    elif isinstance(x,Paper):
        if isinstance(y,Rock):
            return x
        elif isinstance(y, Paper):
            return None
        elif isinstance(y, Scissors):
            return y
        else:
            raise TypeError("Unknown second thing")
    elif isinstance(x, Scissors):
        if isinstance(y,Rock):
            return y
        elif isinstance(x,Paper):
            return x
        elif isinstance(y,Scissors):
            return None
        else:
            raise TypeError("Unknown second thing")
    else:
        raise TypeError("Unknown first thing")

rock,paper,scissors = Rock(),Paper(),Scissors()
