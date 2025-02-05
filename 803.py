def static_app(
        environ: Dict,
        start_response: SR_Func
    ) -> Union[Iterator[bytes],List[bytes]]:
    log = environ['wsgi.errors']
try:
    print(f'CWD={Path.cwd()}',file=log)
    static_path = Path.cwd()/environ['PATH_INFO'][1:]
    with static_path.open() as static_file:
        content = static_file.read().encode("utf-8")
        headers=[("Content-Type",'text/plain;charset="utf-8"'),
                 ("Content-Length",str(len(content)))]
        start_response('200 OK',headers)
        return [content]
except IsAdirectoryError as e:
    return index_app(environ,start_response)
except FileNotFoundError as e:
    start_response('404 NOT FOUND',[])
    return [
        f"Not Found {static_path}\n{e!r}".encode("utf-8")
    ]

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)
