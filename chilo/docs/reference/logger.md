---
title: Logger Reference
---

Below is an example of how to use the logger:

## Basic Usage

```python
import os

from chilo_api import logger

logger.log(level='INFO', log='some log') # level=INFO|DEBUG|WARN|ERROR
```

## Decorator Usage

The Chilo logger also comes packaged as an easy to use log decorator that can decorate any method or function and even apply log conditions so you can
control when exactly something is logged.


```python
from chilo_api import log

@log()
def example_simple(arg1, arg2, **kwargs):
    return {'args': [arg1, arg2], 'kwargs': kwargs}

@log(level='INFO')
def example_level(arg1, arg2, **kwargs):
    return {'args': [arg1, arg2], 'kwargs': kwargs}

@log(level='INFO', condition=some_log_condition)
def example_condition(arg1, arg2, **kwargs):
    return {'args': [arg1, arg2], 'kwargs': kwargs}

def some_log_condition(*args, **kwargs):
    if args[0] == 1:
        return True
    return False
```