#!/usr/bin/env python3


import http.server
import os
import signal
import sys

from threading import Thread


class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_PUT(self):
        print('do PUT')
        length = int(self.headers['Content-Length'])
        request = str(self.rfile.read(length), encoding='utf-8');
        print(request)
        path = os.path.join(self.translate_path(self.path),'output')
        f = open(path,'w')
        f.write(request)
        f.close()
        self.send_response(201, 'Created')
        self.end_headers()

    def do_GET(self):
        print('do GET')
        print(str(self.headers, encoding='utf-8'))
        self.send_response(200)
        self.end_headers()


def start_server(port):
    httpd = http.server.HTTPServer(('', port), HTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    ports = [int(arg) for arg in sys.argv[1:]]
    for port in ports:
        server = Thread(target=start_server, args=[port])
        server.daemon = True
        server.start()
    signal.pause()
