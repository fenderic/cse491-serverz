# Eric Austin - austine5 - fenderic


#!/usr/bin/env python

import random
import socket
import time

def main():

    s = socket.socket()         # Create a socket object
    host = socket.getfqdn()     # Get local machine name
    port = random.randint(8000, 9999)
    s.bind((host, port))        # Bind to the port

    print 'Starting server on', host, port
    print 'The Web server URL for this would be http://%s:%d/' % (host, port)

    s.listen(5)                 # Now wait for client connection.

    print 'Entering infinite loop; hit CTRL-C to exit'
    while True:
        # Establish connection with client.    
        c, (client_host, client_port) = s.accept()
        print 'Got connection from', client_host, client_port

        handle_connection(c)


def handle_connection(c):
    
    req = c.recv(1000)          # Request
    path = req.split('\r\n')[0].split(' ')[1]
                                # Grabbing the path from the request

    if path == '/':

        c.send('HTTP/1.0 200 OK\r\n' + \
                'Content-type: text/html\r\n' + \
                '\r\n' + \
                '<h1>Hello, world.</h1>' + \
                'This is fenderic\'s Web server.' + \
                '<a href= /content>Content</a><br>' + \
                '<a href= /file>File</a><br>' + \
                '<a href= /image>Image</a><br>')

    elif path == '/content':

        c.send('HTTP/1.0 200 OK\r\n' + \
                'Content-type: text/html\r\n' + \
                '\r\n' + \
                '<h1>Content page</h1>' + \
                'words words words')

    elif path == '/file':

        c.send('HTTP/1.0 200 OK\r\n' + \
                'Content-type: text/html\r\n' + \
                '\r\n' + \
                '<h1>File page</h1>' + \
                'cabinet')

    elif path == '/image':

        c.send('HTTP/1.0 200 OK\r\n' + \
                'Content-type: text/html\r\n' + \
                '\r\n' + \
                '<h1>Image page</h1>' + \
                'imagine that')

    c.close()


if __name__ == '__main__':
    main()
