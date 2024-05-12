from typing import Iterable, Iterator
def access_detail_iter(
        access_iter: Iterable[Access]
    ) -> Iterator[AccessDetails]:
    for access in access_iter:
        try:
            meth,url,protocol = parse_request(access.request)
                yield AcessDetails(
                    access = access,
                    time = parse_time(access.time),
                    method = meth,
                    url = urllib.parse.urlparse(url),
                    protocol = protocol,
                    referrer = urllib.parse.urlparse(access.referer),
                    agent = parse_agent(access.user_agent)
                )
        except ValueError as e:
            print(e,repr(access))
