def authorize(request, response, _):
    if not request.headers.get('x-api-key'):
        response.code = 401
        response.set_error('headers', 'unauthorized access')
