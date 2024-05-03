import decimal
from typing import Callable,Optional,Any,TypeVar,cast

FuncType = Callable[...,Any]
F = TypeVar('F',bound=FuncType)

def bad_data(function:F) -> F:
    @wraps(function)
    def wrap_bad_data(text:str,*args:Any,**kw:Any) -> Any:
        try:
            return function(text,*args,**kw)
        except (ValueError,decimal.InvalidOperation):
            cleaned = text.replace(",","")
            return function(cleaned,*args,*kw)
    return cast(F,wrap_bad_data)
