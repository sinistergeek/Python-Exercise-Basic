import arith_funcs

def test_add():
    assert arith_funcs.add(10,20) == 30

def test_subtract():
    assert arith_funcs.subtract(10,20) == -10
def test_multiply():
    assert arith_funcs.multiply(10,20) == 200
    def test_divide():
        assert arith_funcs.divide(10,0) == "invalid denominator"
        assert arith_funcs.divide(10,5) == 2
