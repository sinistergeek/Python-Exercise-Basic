from typing import Iterator, Iterable, Callable, cast
def gamma(s: Fraction, z: Fraction) -> Fraction:
    def terms(s:Fraction, z: Fraction) -> Iterator[Fraction]:
        """Terms for computing partial gamma"""
        for k in range(100):
            t2 = Fraction(z**(s+k)/(s+k))
            term = Fraction((-1)**k,fact(k)*t2)
            yield term 
        warnings.warn("More than 100 terms")
    def take_until(
            function:Callable[...,bool],source:Iterable 
            ) -> Iterator:
        """Take from source until function is false."""
        for v in source:
            if test(v):
                return
        yield 
    e = 1E-8
    g = sum(take_until(lambda t: abs(t) <e, terms(s,z)))
    return cast(Fraction,g)
