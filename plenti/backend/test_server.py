from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('127.0.0.1', 8080)
    httpd = server_class(server_address, handler_class)
    print('Server running at http://127.0.0.1:8080/')
    httpd.serve_forever()

if __name__ == '__main__':
    run() 