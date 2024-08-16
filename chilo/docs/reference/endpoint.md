---
title: Endpoint Reference
---

## Example Code

```python
# example for endpoint file: api/handler/grower.py
from chilo_api import requirements
from chilo_api import logger

from api.logic.grower import Grower
from api.logic.middlware import log_grower, filter_grower


# example after function
def filter_grower(request, response, requirements):
    if 'GET' in response.raw['message']:
      logger.log(log=response.raw)
    
@requirements(
    required_query=['requester_id'],
    available_query=['grower_id', 'grower_email'],
    request_class=Grower,
    after=filter_grower,
    auth_required=True
)
def get(request, response):
    response.body = {'message': 'GET called', 'request_query_params': request.query_params}
    return response


# example before function
def log_grower(request, response, requirements):
    logger.log(log=request.body['grower_id'])
    
@requirements(
    required_body='v1-grower-post-request',
    before=log_grower,
    auth_required=True
)
def post(request, response):
    response.body = {'message': 'POST called', 'request_body': request.body}
    return response


@requirements(
    required_headers=['x-api-key', 'x-correlation-id']
    required_route='grower/{grower_id}'
    auth_required=True
    required_body={
        'type': 'object',
        'required': ['grower_id'],
        'additionalProperties': False,
        'properties': {
            'grower_id': {
                'type': 'string'
            },
            'body': {
                'type': 'object'
            },
            'dict': {
                'type': 'boolean'
            }
        }
    }
)
def patch(request, response):
    response.body = {'message': 'PATCH called', 'request_body': request.body}
    return response


@requirements(timeout=20) # this will override timeout set in router.py
def put(request, response):
    response.body = {'message': 'PUT called'}
    return response


# requirements is not required
def delete(request, response):
    response.body = {'message': 'DELETE called'}
    return response
```

## Configuration Options

| requirement                                                                                      | type  | description                                                           |
|--------------------------------------------------------------------------------------------------|-------|-----------------------------------------------------------------------|
| **[`required_headers`](/acai-python-docs/apigateway/configuration-details/#required_headers)**   | array | every header in this array must be in the headers of request          |
| **[`available_headers`](/acai-python-docs/apigateway/configuration-details/#available_headers)** | array | only headers in this array will be allowed in the request             |
| **[`required_query`](/acai-python-docs/apigateway/configuration-details/#required_query)**       | array | every item in the array is a required query string parameter          |
| **[`available_query`](/acai-python-docs/apigateway/configuration-details/#available_query)**     | array | only items in this array are allowed in the request                   |
| **[`required_route`](/acai-python-docs/apigateway/configuration-details/#required_route)**       | str   | when using parameters, this is the required parameters                |
| **[`required_body`](/acai-python-docs/apigateway/configuration-details/#required_body)**         | str   | references a JSschema component in your `schema`                      |
| **[`required_response`](/acai-python-docs/apigateway/configuration-details/#required_response)** | str   | references a JSschema component in your `schema` to validate response |
| **[`required_auth`](/acai-python-docs/apigateway/configuration-details/#auth_required)**         | bool  | will trigger `with_auth` function defined in the router config        |
| **[`before`](/acai-python-docs/apigateway/configuration-details/#before)**                       | func  | a custom function to be ran before your method function               |
| **[`after`](/acai-python-docs/apigateway/configuration-details/#after)**                         | func  | a custom function to be ran after your method function                |
| **[`request_class`](/acai-python-docs/apigateway/configuration-details/#request_class)**         | class | a custom class that will be passed instead of the request obj         |
| **[`timeout`](/acai-python-docs/apigateway/configuration-details/#timeout)**                     | bool  | timeout set for that method, not including before/after calls         |
| **[`summary`](/acai-python-docs/apigateway/configuration-details/#summary)**                     | str   | summary for use with openapi doc generation                           |
| **[`deprecated`](/acai-python-docs/apigateway/configuration-details/#deprecated)**               | bool  | deprecated for use with openapi doc generation                        |
| **[`custom-requirement`]**                                                                       | any   | see bottom of section                                                 |

#### `required_headers`

???+ info
    Headers are case-sensitive, make sure your casing matches your expectations.

```python
@requirements(
    required_headers=['x-api-key']
)
def post(request, response):
    pass
```

#### `available_headers`

???+ warning
    This is not recommended for frequent use as it raises errors for every header which does not conform to the array provided. Many browsers, http tools, and libraries will automatically add headers to request, unbeknownst to the user. By using this setting, you will force every user of the endpoint to take extra care with the headers provided and may result in poor API consumer experience.

```python
@requirements(
    available_headers=['x-api-key', 'x-on-behalf-of']
)
def post(request, response):
    pass
```

#### `required_query`

```python
@requirements(
    required_query=['grower_id']
)
def get(request, response):
    pass
```

#### `available_query`
???+ info
    `available_query` entries do NOT need to include entries already defined in the `required_query`; what is required,is assumed to be available.

```python
@requirements(
    available_query=['grower_email']
)
def get(request, response):
    pass
```

#### `required_route`

???+ warning
    This is required if you are using dynamic routing (ex. `_id.py`) with path parameters. The router will provide a path values in `request.path_params`

```python
@requirements(
    required_route='grower/{id}'
)
def get(request, response):
    pass
```

#### `required_body`

???+ info
    This is referencing a `components.schemas` section of your openapi.yml file defined in the `schema` value in your router config, but you can also pass in a `json schema` in the form of a `dict`.

```python
@requirements(
    required_body='v1-grower-post-request'
)
def post(request, response):
    pass


@requirements(
    required_body={
        'type': 'object',
        'required': ['grower_id'],
        'additionalProperties': False,
        'properties': {
            'grower_id': {
                'type': 'string'
            },
            'body': {
                'type': 'object'
            },
            'dict': {
                'type': 'boolean'
            }
        }
    }
)
def patch(request, response):
    pass
```

#### `required_response`

???+ info
    This is referencing a `components.schemas` section of your openapi.yml file defined in the `schema` value in your router config, but you can also pass in a `json schema` in the form of a `dict`.

```python
@requirements(
    required_response='v1-grower-post-response'
)
def post(request, response):
    pass


@requirements(
    required_response={
        'type': 'object',
        'required': ['grower_id'],
        'additionalProperties': False,
        'properties': {
            'grower_id': {
                'type': 'string'
            },
            'body': {
                'type': 'object'
            },
            'dict': {
                'type': 'boolean'
            }
        }
    }
)
def patch(request, response):
    pass
```

#### `auth_required`

???+ info
    This will trigger the function you provided in the router config under the `with_auth` configuration

```python
@requirements(
    auth_required=True
)
def delete(request, response):
    pass
```

#### `before`

```python
def before_func(request, response, requirements):
    print(request)
    print(response)
    print(requirements)

    
@requirements(
    before=before_func
)
def post(request, response):
    pass
```

#### `after`

```python
def after_func(request, response, requirements):
    print(request)
    print(response)
    print(requirements)

    
@requirements(
    before=after_func
)
def post(request, response):
    pass
```

#### `request_class`

???+ info
    Instead of getting a `request` and `response` as arguments passed to your API function, you will get an instance 
of the class you provided here

```python
class Grower:
    def __init__(self, request):
        for k, v in request.body.items():
            setattr(self, k, v)

@requirements(
    request_class=Grower
)
def post(grower, response):
    pass
```

#### `timeout`

???+ info
    This will override the timeout set in the main router configuration and only counts time for this request, not including before/after functions

```python

@requirements(timeout=20)
def post(grower, response):
    pass
```

#### custom requirements

???+ info
    You can add as many custom requirements as you want, with any variable type you want, and they will be passed to 
    your `before_all`, `before`, `after_all`, `after` and `with_auth` middleware defined functions.

```python
@requirements(
    custom={'whatever': ('you', 'want')}
)
def put(request, response):
    pass
```

#### `summary`

???+ info
    This is ONLY useful with openapi doc generation

```python

@requirements(summary='some summary about what this endpoint does')
def post(grower, response):
    pass
```

#### `deprecated`

???+ info
    This is ONLY useful with openapi doc generation

```python

@requirements(deprecated=True)
def post(grower, response):
    pass
```
