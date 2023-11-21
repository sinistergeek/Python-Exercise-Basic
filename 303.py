from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
import time

def hello_word(environ,start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [{'Content-type','text/plan'}]

    start_response(status,headers)

    return "Hello World" + str(time.time())

port = 8080
httpd = make_server('0.0.0.0',port,hello_word)
print("Serving on port {}...".format(port))
httpd.serve_forever()
