from typing import Iterable, Iterator
def access_detail_iter2(
        access_iter: Iterable[Access]
    ) -> Iterator[AccessDetails]:

def access_detail_builder(access: Access) -> Optional[AccessDetails]:
    try:
        meth,url,protocol = parse_request(
        access=access,
        time=parse_time(access.time),
        method=meth,
        url=urllib.parse.urlparse(uri),
        protocol = protocol,
        referrer = urllib.parse.urlparse(access.referer),
        agent = parse_agent(access.user_agent))
    except ValueError as e:
        print(e,repr(access))
    return None
return filler(
    None,
    map(access_detail_builder,access_iter)
)
