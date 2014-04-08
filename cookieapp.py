def wsgi_app(environ, start_response):
    path = environ['PATH_INFO']

    if path == '/':
        cookie_info = environ.get('HTTP_COOKIE', "")
        cookie_info = "The cookie: %s<p>" % cookie_info

        start_response('200 OK', [('Content-type', 'text/html')])
        return [cookie_info,
                "<a href='/set'>Set Cookie</a> | ",
                "<a href='/del'>Delete Cookie</a>"]

    elif path == '/set':
        start_response('302 Redirect', [
            ('Content-type', 'text/html'),
            ('Location', '/'),
            ('Set-Cookie', 'favorite_color=red')
            ])

        return ["You should have been redirected"]

    elif path == '/del':
        start_response('302 Redirect', [
            ('Content-type', 'text/html'),
            ('Location', '/'),
            ('Set-Cookie', 'favorite_color=NONE; Expires=Thu, 01-Jan-1970 00:00:01 GMT')
            ])

        return ["You should have been redirected"]

    start_response('404 Not Found', [('Content-type', 'text/html')])
    return []
