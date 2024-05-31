from typing import Callable, TypeVar,Any,cast
from functools import wraps
def to_bytes(
        function: Callable[...,str]
    ) -> Callable[...,bytes]:
    @wraps(function)
    def decorated(*args,**kw):
        text = function(*args,**kw)
        return text.encode("utf-8")
    return cast(Callable[...,bytes],decorated)
SERIALIZERS = {
    'xml':('application/xml',serialize_xml),
    'html':('text/html',to_bytes(serialize_html)),
    'json':('application/json'to_bytes(serialize_json)),
    'csv':('text/csv',to_bytes(serialize_csv))
}
