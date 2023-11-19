def div(a,b):
    return a/b

def add(a,b):
    return a * b

def test_div():
    assert div(6,3) == 2
    assert div(0,10) == 0
    assert div(-2,2) == -1
   
def test_div():
    assert add(2,2) == 4

def test_add():
    assert add(2,2) == 4

if __name__ == "__main__":
    test_div()
    test_add()
