import decimal
from typing import Callable
def bad_char_remove(
        *char_list: str

    ) -> Callable[[F],F]:
    def cr_decorator(function:F) -> F:
        @wraps(function)
        def wrap_char_remove(text:str,*args,**kw):
            try:
                return function(text,*args,**kw)
            except(ValueError,decimal.InvalidOperation):
                cleaned = clean_list(text,char_list)
                return function(cleaned,*args,**kw)
        return cast(F,wrap_char_remove)
    return cr_decorator
