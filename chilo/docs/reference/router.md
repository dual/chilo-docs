---
title: Router Refernce
---

## Configuration Options

| option                          | type | required                               | description                                                                                                              |
|---------------------------------|------|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **`after_all`**                 | func | no                                     | will call this function after EVERY request to the API                                                                   |
| **`base_path`**                 | str  | yes                                    | the base path of the API Gateway instance this is running on                                                             |
| **`before_all`**                | func | no                                     | will call this function before EVERY request to the API                                                                  |
| **`cache_mode`**                | str  | no; 'all','static-only','dynamic-only' | will cache route endpoint module (not response), all, static, or dynamic (routes with path variables) endpoints          |
| **`cache_size`**                | int  | no; (default 128)                      | how many endpoint modules to cache                                                                                       |
| **`cors`**                      | bool | no (default True)                      | will open cors to allow hitting from any source (`*`)                                                                    |
| **`handlers`**                  | str  | yes                                    | file path pointing to the directory where the endpoints are                                                              |
| **`host`**                      | str  | no (default 127.0.0.1)                 | host address to run on                                                                                                   |
| **`on_error`**                  | func | no                                     | will call this function on every unhandled error; not including validation errors                                        |
| **`on_timeout`**                | func | no                                     | when timout error is raised, this function will run                                                                      |
| **`openapi_validate_request`**  | bool | no; requires `schema`                  | will automatically validate request against openapi.yml                                                                  |
| **`openapi_validate_response`** | bool | no                                     | will validate response of an endpoint, can effect performance, not recommended for production                            |
| **`output_error`**              | bool | no (default true)                      | will output more detailed error from stacktrace as part of api response; otherwise will only say `internal server error` |
| **`port`**                      | int  | no (default 3000)                      | will output more detailed error from stacktrace as part of api response; otherwise will only say `internal server error` |
| **`schema`**                    | str  | yes, if `openapi_validate_request`     | file path pointing to the location of the openapi.yml file                                                               |
| **`timeout`**                   | int  | no (default `None`)                    | timeout functionality for main handler logic (does not indclude before, after, before_all, after_all)                    |
| **`verbose`**                   | bool | no                                     | will log every setup, every request and every response                                                                   |
| **`when_auth_required`**        | func | no                                     | will call this function when `requirements` decorator have `auth_required` set to `True`                                 |

## Example Code

```python
from chilo_api import Chilo


def before_all(request, response, requirements):
    # will run before every request
    pass


def afrer_all(request, response, requirements):
    # will run after every request
    pass


def when_auth_required(request, response, requirements):
    # will run only when @requirements(auth_required=True)
    pass


def on_error(request, response, requirements):
    # will run on any 5xx level error
    pass


def on_timeout(request, response, requirements):
    # will run on any timeout error
    pass


api = Chilo(
    host='127.0.0.1'
    port=3000
    base_path='/',
    handlers='api/handlers',
    schema='api/openapi.yml',
    openapi_validate_request=True
    openapi_validate_response=True
    reload=True
    verbose=True
    before_all=before_all
    after_all=afrer_all
    when_auth_required=when_auth_required
    on_error=on_error
    on_timeout=on_timeout
    cors=True
    timeout=30
    cache_size=128
    cache_mode='all'
)
```