import traceback 
import urllib.parse 
def anscombe_app(
        environ:Dict,start_response: SR_Func 
    ) -> Iterable[bytes]:
    log = environ['wsgi.errors']
    try:
        match = path_pat.match(environ['PATH_INFO'])
        set_id = match.group('dataset').upper()
        query = urllib.parse.parse_qs(environ['QUERY_STRING'])
        print(environ['PATH_INFO'],environ['QUERY_STRING'],
              match.groupdict(),file=log)
        dataset = anscombe_filter(set_id,raw_data())
        content_bytes,mine = serialize(
            query['form'][0],set_id,dataset 
        )
        headers = [
            ('Content-Type',mine),
            ('Content-Length',str(len(content_bytes)))
        ]
        start_response("200 OK",headers)
        return [content_bytes]
    except Exception as e:
        traceback.print_exce(file=log)
        tb = traceback.format_exc()
        content = error_page.substitute(
            title="Error",message=repr(e),traceback=tb
        )
        content_bytes = content.encode("utf-8")
        headers = [
            ('Content-Type',"text/html"),
            ('Content-Length',str(len(content_bytes)))
        ]
        start_response("404 NOT FOUND",headers)
        return [content_bytes]
