from typing import Callable, Optional, Any

class NullAware:
    def __init__(
            self, some_func: Callable[[Any],Any]) -> None:
        self.some_func = some_func

    def __call__(self, arg: Optional[Any]) -> Optional[Any]:
        return None if arg is None else self. some_func(arg)
