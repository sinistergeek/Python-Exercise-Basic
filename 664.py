from typing import Callable
class Mersenne1:
    def __init__(self,algorith : Callable[[int],int]) -> None:
        self.pow2 = algorithm
    def __call__(self,arg: int) -> int:
        return self.pow2(arg) - 1
