---
title: Request Reference
---
By default, every endpoint function will receive an instance of the `Response` class (aka `response`) as the second argument of their function. 
This response object is meant to provide consistency to HTTP response codes and error signatures. Below is a list and examples of all the properties of the `response`:

### Response Properties

| property                                                                            | type    | description                                                   |
|-------------------------------------------------------------------------------------|---------|---------------------------------------------------------------|
| [`headers`](/acai-python-docs/apigateway/configuration-details/#responseheaders)    | tuple   | provide headers in tuple pairs to add new headers             |
| [`code`](/acai-python-docs/apigateway/configuration-details/#responsecode)          | int     | http response code to be returned the requester               |
| [`body`](/acai-python-docs/apigateway/configuration-details/#responsebody)          | any     | body of the response automatically converted to JSON string   |
| [`raw`](/acai-python-docs/apigateway/configuration-details/#responserawbody)        | any     | body of the response not converted to JSON string             |
| [`compress`](/acai-python-docs/apigateway/configuration-details/#responsecompress)  | bool    | will compress the body if set to true and add proper headers  |
| [`set_error`](/acai-python-docs/apigateway/configuration-details/#responseseterror) | func    | function to set an error with a key and value                 |
| [`has_error`](/acai-python-docs/apigateway/configuration-details/#responsehaserror) | boolean | simple property to check if response already has errors in it |


#### `response.headers`

```python
response.headers = ('status', 'ok')
response.headers = ('response_id', 'some-guid')

print(response.headers)

# output:
{
    'status': 'ok',
    'response_id': 'some-guid',
}
```

#### `response.code`

```python
response.code = 418;

print(response.code);

# output:
418
```

#### `response.body`

???+ info
    This will automatically convert the body to json if possible when called.

```python
response.body = {'some_key': 'some_value'}

print(response.body)

# output:
'{"someKey":"someValue"}'
```

#### `response.raw`

???+ info
    This will NOT automatically convert the body to json if possible when called. This is great when working with an `after_all` method that wants to mutate the body of the response before returning to the user.

```python
response.raw = {'some_key': 'some_value'};

print(response.raw)

# output:
{
    'some_key': 'some_value'
}
```

#### `response.compress`

???+ info
    This will compress whatever is in the body property.

```python
response.compress = True

print(response.body)
# output: this will gzip and compress the body.
```

#### `response.set_error(key, value)`

```python
some_key = 'abc123'
response.set_error('someKey', f'{some_key} is not a valid key to use with this service; try again with a different key')
another_key = 'def456'
response.set_error('anotherKey', f'{another_key} is not the correct type to operate on')

print(response.raw)

# output:
{
    'errors': [
        {
            'key_path': 'someKey',
            'message': 'abc123 is not a valid key to use with this service; try again with a different key'
        },
        {
            'key_path': 'anotherKey',
            'message': 'def456 is not the correct type to operate on'
        }
    ]
}
```

#### `response.has_error`

```python
response.setError('user', 'your access is denied')
print(response.has_error)

# output:
True


response.body = {'user': 'you have been granted access'};
print(response.has_error)

# output:
False
```