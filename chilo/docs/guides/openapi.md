---
title: Generating An OpenAPI
---

You can generate a openapi yaml and/or json doc from your existing codebase. This feature can also add to existing openapi docs and/or overwrite
incorrect documentation.

#### command

```shell
python -m chilo generate-openapi --api=api --output=tests/outputs --format=yml,json --delete
```

#### output

```shell
STARTED
generating openapi docs...
validating arguments received...
arguments validated...
scanning handlers: tests/mocks/apigateway/openapi/**/*.py...
importing handler endpoint modules...
deleting paths and methods not found in code base
writing openapi doc to requested directory: tests/outputs
COMPLETED
```

#### options

```shell
--handlers (-l): directory or pattern location of your handlers
--base (-b): (optional) base path of the api url; default='/'
--output (-o): (optional) directory location to save openapi file; defaults handlers directory location
--format (-f): (optional) comma deliminted format options (yml, json)
--delete (-d): (optional) will delete routes and methods in existing openapi doc not found in code base
```