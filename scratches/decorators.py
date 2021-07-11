#python decorator examples

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        value = func(*args,**kwargs)
        print("Count!")
        return value

    return wrapper_decorator




