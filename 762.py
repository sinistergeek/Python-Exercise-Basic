from typing import Callable


def cleanse_before(
        cleanse_function: Callable
    ) -> Callable[F],[F]:
    def abstract_decorator(converter:F) ->F:
        @wraps(converter)
        def cc_wrapper(text:str,*args,**kw) -> Any:
            try:
                return converter(text,*args,**kw)
            except(ValueError,decimal.InvalidOperation):
                cleaned = cleanse_function(text)
                return converter(cleaned,*args,**kw)
        return cast(F,cc_wrapper)
    return abstract_decorator
