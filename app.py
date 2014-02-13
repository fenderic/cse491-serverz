# from http://docs.python.org/2/library/wsgiref.html

#import jinja2

from wsgiref.util import setup_testing_defaults

import jinja2
import cgi
# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    loader = jinja2.FileSystemLoader('./templates')
    env = jinja2.Environment(loader=loader)


    status = '200 OK'
    headers = [('Content-type', 'text/html')]

    start_response(status, headers)

    ret = ["%s: %s\n" % (key, value)
           for key, value in environ.iteritems()]
    ret.insert(0, "This is your environ.  Hello, world!\n\n")

    
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    
    print path

    if method == "POST":
        
        if path == '/':
            
            return handle_index('', env)


        elif path == '/submit':
            
            #return handle_submit_post('', env)
            #return handle_submit_post(form, env)
            return handle_submit_post(environ, env)


        else:

            return handle_404('', env)


    elif method == "GET":

        if path == '/':

            return handle_index('', env)


        elif path == '/content':

            return handle_content('', env)


        elif path == '/file':

            return handle_file('', env)


        elif path == '/image':

            return handle_image('', env)


        elif path == '/submit':

            return handle_submit_get(environ, env)


        else:
            
            return handle_404('', env)


    else:

        return handle_404('', env)


    #printing out the garbage at the top
    return ret



def make_app():

    return simple_app



def handle_index(params, env):

    return str(env.get_template('index.html').render())


def handle_content(params, env):

    return str(env.get_template('content.html').render())


def handle_file(params, env):

    return str(env.get_template('file.html').render())


def handle_image(params, env):

    return str(env.get_template('image.html').render())


def handle_404(params, env):

    return str(env.get_template('404.html').render())


def handle_submit_get(params, env):

    namestring = params['QUERY_STRING']
    namestring = namestring.split('&')

    first_name = namestring[0].split('=')[1]
    last_name = namestring[1].split('=')[1]
    name = dict(first_name = first_name, last_name = last_name)

    return str(env.get_template('submit.html').render(name))


def handle_submit_post(environ, env):

    
    headers = {}
    for i in environ.keys():
        headers[i.lower()] = environ[i]

    print "before form!!!!!"
    print "before headers"
    print headers
    print "after headers"
    print "environ['wsgi.input']"
    print environ['wsgi.input']
    print "environ"
    print environ

    # breaking on something here.......

    form = cgi.FieldStorage(headers = headers, fp = environ['wsgi.input'], environ = environ)

    print "after form!!!!"

    first_name = form['firstname'].value
    last_name = form['lastname'].value
    name = dict(first_name = first_name, last_name = last_name)

    return str(env.get_template('submit.html').render(name))



