#!/usr/bin/env python3


import http.server
import os
import signal
import socketserver
import sys
import socket

from threading import Thread


clients = []


class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_PUT(self):
        length = int(self.headers['Content-Length'])
        data = str(self.rfile.read(length), encoding='utf-8')
        for client in clients:
            client.send(data)
        path = os.path.join(self.translate_path(self.path),'output')
        f = open(path,'w')
        f.write(data)
        f.close()
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        data = str(self.headers, encoding='utf-8')
        for client in clients:
            try:
                client.send(data)
            except:
                pass
        self.send_response(200)
        self.end_headers()


def start_server(port):
    httpd = http.server.HTTPServer(('', port), HTTPRequestHandler)
    httpd.serve_forever()


def start_tcp_server(port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('', port))
    serversocket.listen(10)
    while True:
        (clientsocket, clientaddr) = serversocket.accept()
        print(clientaddr,"!!!")
        clients.append(clientsocket)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage <port tcp> <port a> <port b>')
        sys.exit(1)
    ports = [int(arg) for arg in sys.argv[2:]]
    for port in ports:
        server = Thread(target=start_server, args=[port])
        server.daemon = True
        server.start()
    tcp_server = Thread(target=start_tcp_server, args=[int(sys.argv[1])])
    tcp_server.daemon = True
    tcp_server.start()
    signal.pause()
