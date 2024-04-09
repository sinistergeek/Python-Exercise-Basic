from typing import Callable, List, Optional
R_Text = List[Optional[Text]]
R_Float = List[Optional[float]]
float_row: Callable[[R_Text],R_Float] = lambda row: list(map(float_none, row))
