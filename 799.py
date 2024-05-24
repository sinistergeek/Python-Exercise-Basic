from http.server import HTTPServer,def server_demo():
    httpd = HTTPServer(
    ('localhost',8080),SimpleHTTPRequestHandler)
while True:
    httpd.handle_request()
httpd.shutdown()
