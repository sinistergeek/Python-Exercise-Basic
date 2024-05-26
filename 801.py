from typing import(
    Dict,Callable,List,Tuple,Iterator,Union,Optional 
)
from mypy_extensions import DefaultArg 
SR_Func = Callable[[str,List[Tuple[str,str]],DefaultArg(Tuple)],None]
def static_app(
        environ:Dict,
        start_response: SR_Func

    ) -> Union[Iterator[bytes],List[bytes]]:
