# Eric Austin - austine5 - fenderic


#!/usr/bin/env python

import random
import socket
import time
import urlparse

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
    
    req = c.recv(1000)                          # Request
    req_line = req.split('\r\n')[0].split(' ')  # Request Line

    method = req_line[0]                        # HTTP Method

    parsed_url = urlparse.urlparse(req_line[1]) # Parsed URL
    path = parsed_url[2]                        # Path


    if method == 'POST':

#        c.send('HTTP/1.0 200 OK\r\n' + \
#                'Content-type: text/html\r\n' + \
#                '\r\n' + \
#                'got a POST')

        if path == '/':

            handle_index(c,'')

        elif path == '/submit':

            handle_submit(c,req.split('\r\n')[-1])


    else:

        if path == '/':

            handle_index(c,'')

        elif path == '/content':

            handle_content(c,'')

        elif path == '/file':

            handle_file(c,'')

        elif path == '/image':

            handle_image(c,'')

        elif path == '/submit':

            handle_submit(c, parsed_url[4])

            

    c.close()



def handle_index(c, params):

    c.send('HTTP/1.0 200 OK\r\n' + \
            'Content-type: text/html\r\n' + \
            '\r\n' + \
            '<h1>Hello, world.</h1>' + \
            'This is fenderic\'s Web server.<br>' + \
            '<a href= /content>Content</a><br>' + \
            '<a href= /file>File</a><br>' + \
            '<a href= /image>Image</a><br>' + \
            'GET Form' + \
            '<form action="/submit" method="GET">\n' + \
            '<p>First Name: <input type="text" name="firstname"></p>\n' + \
            '<p>Last Name: <input type="text" name="lastname"></p>\n' + \
            '<input type="submit" value="Submit">\n\n' + \
            '</form>' + \
            'POST Form' + \
            '<form action="/submit" method="POST">\n' + \
            '<p>First Name: <input type="text" name="firstname"></p>\n' + \
            '<p>Last Name: <input type="text" name="lastname"></p>\n' + \
            '<input type="submit" value="Submit">\n\n' + \
            '</form>')


def handle_content(c, params):
    
    c.send('HTTP/1.0 200 OK\r\n' + \
            'Content-type: text/html\r\n' + \
            '\r\n' + \
            '<h1>Content page</h1>' + \
            'words words words')


def handle_file(c, params):

    c.send('HTTP/1.0 200 OK\r\n' + \
            'Content-type: text/html\r\n' + \
            '\r\n' + \
            '<h1>File page</h1>' + \
            'cabinet')


def handle_image(c, params):
    
    c.send('HTTP/1.0 200 OK\r\n' + \
            'Content-type: text/html\r\n' + \
            '\r\n' + \
            '<h1>Image page</h1>' + \
            'imagine that')


def handle_submit(c, params):

    namestring = params.split('&')

    first_name = namestring[0].split('=')[1]
    last_name = namestring[1].split('=')[1]

    c.send('HTTP/1.0 200 OK\r\n' + \
            'Content-type: text/html\r\n' + \
            '\r\n' + \
            'Hello Mr. %s %s.' % (first_name, last_name))



if __name__ == '__main__':
    main()
