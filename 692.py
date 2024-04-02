from multipledispatch  import dispatch

@dispatch(Rock, Rock)
def beats3(x,y): return None

@dispatch(Rock, Paper)
def beats3(x,y): return y

@dispatch(Rock,Scissors)
def beats3(x,y): return x

@dispatch(Paper,Rock)
def beats3(x,y): return x

@dispatch(Paper,Paper)
def beats3(x,y): return None

@dispatch(Paper, Scissors)
def beats3(x,y): return x

@dispatch(Scissors, Rock)
def beats3(x,y): return y

@dispatch(Scissors, Paper)
def beats3(x,y): return x

@dispatch(Scissors,Scissors)
def beats3(x,y): return None

@dispatch(object,object)
def beats3(x,y):
    if not isinstance(x,(Rock, Paper, Scissors)):
        raise TypeError("Unknown first thing")
    else:
        raise TypeError("Unknown second thing")
