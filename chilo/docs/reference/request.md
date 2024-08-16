---
title: Request Reference
---

By default, every endpoint function will receive an instance of the `Request` class (aka `request`) as the first 
argument of their function. This `request` has a lot of properties which will do common things automatically, but 
still allows the developer to override those operations if they deem necessary. Below is a list and examples of all 
the properties of the `request`:

### Request Properties

| property                                                                                  |  type  | mutable | description                                                   |
|:------------------------------------------------------------------------------------------|:------:|:-------:|:--------------------------------------------------------------|
| [`method`](/acai-python-docs/apigateway/configuration-details/#requestmethod)             |  str   |   no    | the http method of the request                                |
| [`cookies`](/acai-python-docs/apigateway/configuration-details/#requestcookies)           |  list  |   no    | the cookies of the request                                    |
| [`protocol`](/acai-python-docs/apigateway/configuration-details/#requestprotocol)         |  str   |   no    | the protocol of the request                                   |
| [`content_type`](/acai-python-docs/apigateway/configuration-details/#requestcontent_type) |  str   |   no    | the content_type of the request body                          |
| [`host_url`](/acai-python-docs/apigateway/configuration-details/#requesthost_url)         |  str   |   no    | the host_url of the request was sent to                       |
| [`domain`](/acai-python-docs/apigateway/configuration-details/#requestdomain)             |  str   |   no    | the domain of the request was sent to                         |
| [`stage`](/acai-python-docs/apigateway/configuration-details/#requeststage)               |  str   |   no    | the stage the lambda was deployed to                          |
| [`resource`](/acai-python-docs/apigateway/configuration-details/#requestresource)         |  str   |   no    | the AWS resource being invoked                                |
| [`authorizer`](/acai-python-docs/apigateway/configuration-details/#requestauthorizer)     | object |   no    | if using a customized authorizer, the authorizer object       |
| [`headers`](/acai-python-docs/apigateway/configuration-details/#requestheaders)           | object |   no    | the headers of the request                                    |
| [`params`](/acai-python-docs/apigateway/configuration-details/#requestparams)             | object |   no    | combination of query string and path params in one object     |
| [`query_params`](/acai-python-docs/apigateway/configuration-details/#requestquery_params) | object |   no    | query string parameters from the request                      |
| [`path_params`](/acai-python-docs/apigateway/configuration-details/#requestpath_params)   | object |   no    | the path parameters of the request                            |
| [`route`](/acai-python-docs/apigateway/configuration-details/#requestroute)               |  str   |   no    | the requested route with placeholders of params               |
| [`path`](/acai-python-docs/apigateway/configuration-details/#requestpath)                 |  str   |   no    | the raw requested path with actual param values               |
| [`json`](/acai-python-docs/apigateway/configuration-details/#requestjson)                 | object |   no    | the body of the request, converted from json string in object |
| [`xml`](/acai-python-docs/apigateway/configuration-details/#requestxml)                   | object |   no    | the body of the request, converted from xml string in object  |
| [`graphql`](/acai-python-docs/apigateway/configuration-details/#requestgraphql)           |  str   |   no    | the body of the graphql request as a string                   |
| [`body`](/acai-python-docs/apigateway/configuration-details/#requestbody)                 |  any   |   no    | the body of the request, converted to based on data type      |
| [`raw`](/acai-python-docs/apigateway/configuration-details/#requestraw)                   |  any   |   no    | the raw body of the request no conversion                     |
| [`context`](/acai-python-docs/apigateway/configuration-details/#requestcontext)           | object |   yes   | mutable request context to assigned and pass around           |

#### `request.cookies`

```python
print(request.cookies)

# output: 
['some-cookie']
```

#### `request.protocol`

```python
print(request.protocol)

# output: 
'https'
```

#### `request.content_type`

```python
print(request.content_type)

# output: 
'application/json'
```

#### `request.host_url`

```python
print(request.host_url)

# output: 
'https://api.are-great.com'
```

#### `request.domain`

```python
print(request.domain)

# output: 
'api.are-great.com'
```

#### `request.stage`

```python
print(request.stage)

# output: 
'prod'
```

#### `request.method`

```python
print(request.method)

# output: 
'get'
```

#### `request.resource`

```python
print(request.resource)

# output: 
'/{proxy+}'
```

#### `request.authorizer`

???+ tip
    This is only useful if you are using an external authorizer with your lambda.

```python
print(request.authorizer)

# output:
{
    'apiKey': 'SOME KEY',
    'userId': 'x-1-3-4',
    'correlationId': 'abc12312',
    'principalId': '9de3f415a97e410386dbef146e88744e',
    'integrationLatency': 572
}
```

#### `request.headers`

```python
print(request.headers)

# output:
{
    'x-api-key': 'SOME-KEY',
    'content-type': 'application/json'
}
```

#### `request.params`

???+ info
    This combines both path parameters and query string parameters, nested in one object.

```python
print(request.params)

# output:
{
    'query': {
        'name': 'me'
    },
    'path': {
        'id': 1
    }
}
```

#### `request.query_params`

```python
print(request.query_params)

# output:
{
     'name': 'me'
}
```

#### `request.path_params`

```python

print(request.path_params)

# output:
{
     'id': 1
}
```

#### `request.route`

???+ info
    This will provide the route with the path param variables included

```python

print(request.route)

# output:
'grower/{id}'
```

#### `request.path`

???+ info
    This will provide the route with the path param values replacing the variables

```python
print(request.path)

# example output: 
'grower/1'
```

#### `request.json`

???+ warning
    This will raise an unhandled exception if the body is not json compatible

```python

print(request.json);

# output:
{
    'some_json_key': 'some_json_value'
}
```

```python

print(request.form);

# output:
{
    'some_form_key': 'some_form_value'
}
```

#### `request.xml`

???+ warning
    This will raise an unhandled exception if the body is not xml compatible

```python
python(request.xml);

# output:
{
    'some_xml_key': 'some_xml_value'
}
```


#### `request.graphql`

???+ info
    This is graphql string since there is no object equivalent; you can pass this directly to your graphql resolver

```python

python(request.graphql);

# output:
'{
    players {
        name
    }
}'
```

#### `request.body`

???+ tip
    This is the safest way to get the body of the request. It will use the `content-type` header to determine the data sent and convert it; if the data can't be converted for whatever reason it will catch the error and return the raw body provided unconverted.

```python

print(request.body)

# output:
{
    'some_key': 'some_value'
}
```


#### `request.raw`

```python

print(request.raw)

# output: 
# whatever the raw data of the body is; string, json string, xml, binary, etc
```


#### `request.context`

???+ tip
    This is the only mutable property of the request, to be used by any of the `before` or `before_all` middleware options

```python

request.context = {'application_assignable': true}
print(request.context)

# output:
{
    'application_assignable': true
}
```
