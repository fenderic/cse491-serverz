# Eric Austin - austine5 - fenderic


#!/usr/bin/env python

import random
import socket
import time
import urlparse
import cgi
import jinja2
from StringIO import StringIO
#import jinja2

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
    
    loader = jinja2.FileSystemLoader('./templates')
    env = jinja2.Environment(loader=loader)

    req = c.recv(1)                             # Request

    while req[-4:] != '\r\n\r\n':
        req += c.recv(1)

    req_line = req.split('\r\n')[0].split(' ')  # Request Line

    method = req_line[0]                        # HTTP Method

    try:
        parsed_url = urlparse.urlparse(req_line[1]) # Parsed URL
        path = parsed_url[2]                        # Path
    except:
        path = "/404"
        notfound(c,'', env)
        return

    if method == 'POST':

        head_dict, content = parse_post_req(c, req)

        environ = {}
        environ['REQUEST_METHOD'] = 'POST'

        form = cgi.FieldStorage(headers = head_dict, fp = StringIO(content), environ = environ)

        if path == '/':

            handle_index(c, '', env)

        elif path == '/submit':

            handle_submit_post(c, form, env)

        else:
            handle_404(c, '', env)
    else:


        if path == '/':

            handle_index(c, '', env)

        elif path == '/content':

            handle_content(c, '', env)

        elif path == '/file':

            handle_file(c, '', env)

        elif path == '/image':

            handle_image(c, '', env)

        elif path == '/submit':

            handle_submit_get(c, parsed_url[4], env)

        else:
            handle_404(c, '', env)

    c.close()



def handle_index(c, params, env):

    response = 'HTTP/1.0 200 OK\r\n' + \
            'Content-type: text/html\r\n' + \
            '\r\n' + \
            env.get_template('index.html').render()

    c.send(response)
#            '<h1>Hello, world.</h1>' + \
#            'This is fenderic\'s Web server.<br>' + \
#            '<a href= /content>Content</a><br>' + \
#            '<a href= /file>File</a><br>' + \
#            '<a href= /image>Image</a><br>' + \
#            '<br> GET Form' + \
#            '<form action="/submit" method="GET">\n' + \
#            '<p>First Name: <input type="text" name="firstname"></p>\n' + \
#            '<p>Last Name: <input type="text" name="lastname"></p>\n' + \
#            '<input type="submit" value="Submit">\n\n' + \
#            '</form>' + \
#            '<br> POST Form' + \
#            '<form action="/submit" method="POST">\n' + \
#            '<p>First Name: <input type="text" name="firstname"></p>\n' + \
#            '<p>Last Name: <input type="text" name="lastname"></p>\n' + \
#            '<input type="submit" value="Submit">\n\n' + \
#            '</form>' + \
#            '<br> POST Form (multipart/form-data)' + \
#            '<form action="/submit" method="POST" enctype="multipart/form-data">\n' + \
#            '<p>First Name: <input type="text" name="firstname"></p>\n' + \
#            '<p>Last Name: <input type="text" name="lastname"></p>\n' + \
#            '<input type="submit" value="Submit">\n\n' + \
#            '</form>')


def handle_content(c, params, env):
    
    response = 'HTTP/1.0 200 OK\r\n' + \
            'Content-type: text/html\r\n' + \
            '\r\n' + \
            env.get_template('content.html').render()
#            '<h1>Content page</h1>' + \
#            'words words words')

    c.send(response)


def handle_file(c, params, env):

    response = 'HTTP/1.0 200 OK\r\n' + \
            'Content-type: text/html\r\n' + \
            '\r\n' + \
            env.get_template('file.html').render()
#            '<h1>File page</h1>' + \
#            'cabinet')

    c.send(response)


def handle_image(c, params, env):
    
    response = 'HTTP/1.0 200 OK\r\n' + \
            'Content-type: text/html\r\n' + \
            '\r\n' + \
            env.get_template('image.html').render()
#            '<h1>Image page</h1>' + \
#            'imagine that')

    c.send(response)

def handle_submit_get(c, params, env):

    namestring = params.split('&')

    first_name = namestring[0].split('=')[1]
    last_name = namestring[1].split('=')[1]
 
    vars = dict(first_name = first_name, last_name = last_name)
    template = env.get_template('submit.html')


    response = 'HTTP/1.0 200 OK\r\n' + \
            'Content-type: text/html\r\n' + \
            '\r\n' + \
            env.get_template('submit.html').render(vars)
#            'Hello Mr. %s %s.' % (first_name, last_name))

    c.send(response)

def handle_submit_post(c, form, env):

    first_name = form['firstname'].value
    last_name = form['lastname'].value
 
    vars = dict(first_name = first_name, last_name = last_name)
    template = env.get_template('submit.html')


    response = 'HTTP/1.0 200 OK\r\n' + \
            'Content-type: text/html\r\n' + \
            '\r\n' + \
            env.get_template('submit.html').render(vars)
#            'Hello Mr. %s %s.' % (first_name, last_name))

    c.send(response)
   

def handle_404(c, params, env):

    response = 'HTTP/1.0 404 Not Found\r\n' + \
            'Content-type: text/html\r\n' + \
            '\r\n' + \
            env.get_template('404.html').render()

    c.send(response)


def parse_post_req(c, req):

    head_dict = dict()

    req_split = req.split('\r\n')


    for i in range(1, len(req_split) -2):
        header = req_split[i].split(": ", 1)
        head_dict[header[0].lower()] = header[1]

    content_length = int(head_dict['content-length'])

    content = ''
    for i in range(0,content_length):
        content += c.recv(1)

    return head_dict, content

if __name__ == '__main__':
    main()
