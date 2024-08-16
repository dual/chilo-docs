---
title: Building an Endpoint
---

# How to build endpoints

Each endpoint is meant to be treated as a separate module within the API.Every endpoint file should contain a function which matches an 
[HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) in lower case. 
Most common are `post`, `get`, `put`, `patch`, `delete`; this library does support custom methods, 
if you so choose. As long as the method of the request matches the function name, it will work.

Each method within the endpoint file can have individual validation requirements. These requirements allow you to test 
all structural points of the request, with the ability to use JSONSchema and custom middleware to further extend the 
validation options as well as add additional logic to verify data beyond structural and data-type requirements.

```python
# example for endpoint file: api/handler/grower.py
from chilo_api import requirements


def filter_grower(request, response, requirements):
    if 'GET' in response.raw['message']:
      logger.log(log=response.raw)
    
@requirements(
    required_query=['requester_id'],
    available_query=['grower_id', 'grower_email'],
    required_body='v1-grower-post-request', # refence to openapi.yml
    request_class=Grower,
    before=log_grower,
    after=filter_grower,
    auth_required=True
)
def post(request, response):
    response.body = {'message': 'GET called', 'request_query_params': request.query_params}
    return response
```