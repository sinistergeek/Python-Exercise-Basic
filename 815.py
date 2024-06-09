sqrt_pi = Fraction(677_622_787,382_307_718)
from typing import Union 
def Gamma_Half(
        k: Union[int,Fraction]
    ) -> Union[int,Fraction]:
    if isinstance(k,int):
        return fact(k-1)
    elif isinstance(k,Fraction):
        if k.denominator == 1:
            return fact(k-1)
        elif k.denominator == 2:
            n = k-Fraction(1,2)
            return fact(2*n)/(Fraction(4**n) * fact(n))*sqrt_pi 
    raise ValueError(f"Can't compute ({k})")
