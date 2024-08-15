# Chilo
Chilo, short for chilorhinophis (meaning two headed snake), is a lightweight, form-meets-function, opinionated (yet highly configurable) api framework.

## Benefits
* No route definitions needed; route based on your directory structure
* Built-in OpenAPI request and response validation
* Ease of use with gunicorn
* Generate OpenAPI spec from code base
* Infinitely customizable with middleware extensions

## Philosophy

The Chilo philosophy is to provide a dry, configurable, declarative framework, which encourages Happy Path Programming (HPP).

Happy Path Programming is an idea in which inputs are all validated before operated on. This ensures code follows the happy path without the need for mid-level, nested exceptions and all the nasty exception handling that comes with that. The library uses layers of customizable middleware options to allow a developer to easily dictate what constitutes a valid input, without nested conditionals, try/catch blocks or other coding blocks which distract from the happy path which covers the majority of the source code's intended operation.


## Installation

### Requirements

* Python 3.8 or higher; [download and install Python](https://www.python.org/downloads/)
* Access to public [python registry](https://pypi.org/)

=== "Shell"
```bash
$ pip install chilo_api
# pipenv install chilo_api
# poetry add chilo_api
```

## Quick Start

### 1. Create `main.py`

```python
from chilo_api import Chilo


api = Chilo(
    base_path='/',
    handlers='api/handlers',
)
```

### 2. Create First Handler

???+ tip
    Remember your directory stucture dictates your routes; `__init__.py` will default to the index of that route if it ends in slash

`{PWD}/api/handlers/__init__.py`
```python
def get(request, response):
    response.body = {'hello': 'world'}
    return response
```

### 3. Run your API

```bash
python -m chilo_api serve --api=main --reload=true
```

### 4. Checkout your API

[http://127.0.0.1:3000/](http://127.0.0.1:3000/)

### 5. Validate Your Endpoint (optional)

```python
from chilo_api import requirements


@requirements(required_params=['greeting'])
def get(request, response):
    response.body = {'hello': request.query_params['greeting']}
    return response
```

### 4. Checkout your API (again)

[http://127.0.0.1:3000/?greeting=developer](http://127.0.0.1:3000/?greeting=developer)
