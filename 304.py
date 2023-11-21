from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [{'Content-type','text/plain'}]

    start_response(status,headers)

    ret = ["{}: {}\n".format(key,value)
           for key,value in environ.iteritems()]
    return ret
httpd = make_server('',8080,simple_app)
print("Serving on port 8000....")
httpd.serve_forever()
