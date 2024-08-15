---
title: Features
description: Full list of Features
---

# Features

## Routing

Chilo uses your directory structure as your api routes. This means you don't have to worry about manually setting routes or decorating
functions, which might overlap, during your development process. You just need create the handler file in the desired location.

=== "file/directory structure"

    ```
    ~~ Directory ~~                         ~~ Route ~~
    ==================================================================================
    📦api/                                  |          
    │---📂handlers                          |           
        │---stores.py                       | /stores    
        │---📂item                          |
            │---📜__init__.py               | /item
            │---📜_item_id.py               | /item/{item_id}
        │---📂users                         |
            │---📜__init__.py               | /users
            │---📂_user_id                  |
                │---📜__init__.py           | /users/{user_id}
                │---📂settings              |
                    │---📜__init__.py       | /users/{user_id}/settings
                    │---📜_settings_id.py   | /users/{user_id}/settings/{settings_id}
    ```

### Configuration Options

Chilo allows you to extend and customize how the router works though its many configurations and middleware options. Below are the full list of configurations available

```python
from chilo_api import Chilo


def before_all(request, response, requirements):
    pass


def afrer_all(request, response, requirements):
    pass


def when_auth_required(request, response, requirements):
    pass


def on_error(request, response, requirements):
    pass


def on_timeout(request, response, requirements):
    pass


api = Chilo(
    host='127.0.0.1' # host url to run the api on (default is 127.0.0.1)
    port=3000 # default to port to run (default is 3000)
    base_path='/', # base path of the url to route from (ex. http://locahost/{base_path}/your-endpoint)
    handlers='api/handlers', # glob pattern location of the handler files eligible for being a handler
    schema='api/openapi.yml', # if you have existing openapi you want to use for validations
    openapi_validate_request=True #determines if api should validate request against spece openapi spec (default is False)
    openapi_validate_response=True # determines if api should validate response against spece openapi spec (default is False)
    reload=True # determines if system will watch files and automatically reload (default is False)
    verbose=True # determines if verbose logging is enabled (default is False)
    before_all=before_all # function to run before all requests
    after_all=afrer_all # function to run after all requests; if not errors were detected
    when_auth_required=when_auth_required # function to run when `auth_required` is true on the endpoint requirements dectorator
    on_error=on_error # function to run when 500 level is raised
    on_timeout=on_timeout # function to run when timeout error is raised
    cors=True # determines if cors is enabled (default is True)
    timeout=30 # global value to timeout all handlers after certain amout of time (default is None)
    cache_size=128 # size of the router cache (NOT response cache); allows for faster routing (default is 128)
    cache_mode='all' # determies if router caches all routes or just static or dynamic routes (default is all)
)
```


| option                          | type | required                               | description                                                                                                                                       |
|---------------------------------|------|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **`with_auth`**                 | func | no                                     | will call this function when `requirements` decorator have `auth_required` set to `True`                                                          |
| **`verbose_logging`**           | bool | no                                     | will log every setup, every request and every response                                                                                            |
| **`openapi_validate_response`** | bool | no                                     | will validate response of an endpoint, can effect performance, not recommended for production                                                     |
| **`timeout`**                   | int  | no (default `None`)                    | timeout functionality for main handler logic (does not indclude before, after, before_all, after_all)                                             |
| **`schema`**                    | str  | yes, if `openapi_validate_request`     | file path pointing to the location of the openapi.yml file                                                                                        |
| **`output_error`**              | bool | no (default: true)                     | will output more detailed error from stacktrace as part of api response; otherwise will only say `internal server error`                          |
| **`openapi_validate_request`**  | bool | no; requires `schema`                  | will automatically validate request against openapi.yml                                                                                           |
| **`on_timeout`**                | func | no                                     | when timout error is raised, this function will run                                                                                               |
| **`on_error`**                  | func | no                                     | will call this function on every unhandled error; not including validation errors                                                                 |
| **`handlers`**                  | str  | yes                                    | file path pointing to the directory where the endpoints are                                                                                       |
| **`cors`**                      | bool | no (default True)                      | will open cors to allow hitting from any source (`*`)                                                                                             |
| **`cache_size`**                | int  | no; (default 128)                      | how many endpoint modules to cache                                                                                                                |
| **`cache_mode`**                | str  | no; 'all','static-only','dynamic-only' | will cache route endpoint module (not response) based on option, all (default), static endpoints or dynamic endpoints (route with path variables) |
| **`before_all`**                | func | no                                     | will call this function before EVERY request to the API                                                                                           |
| **`base_path`**                 | str  | yes                                    | the base path of the API Gateway instance this is running on                                                                                      |
| **`after_all`**                 | func | no                                     | will call this function after EVERY request to the API                                                                                            |
