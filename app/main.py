from typing import Callable, Any
from functools import wraps

cache_dict = {}


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        curr_dict = {}
        if cache_dict.get(func.__name__, None) is None:
            cache_dict[func.__name__] = {}
        curr_dict = cache_dict[func.__name__]
        if curr_dict.get(tuple(args), None) is None:
            print("Calculating new result")
            curr_dict[tuple(args)] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return curr_dict[tuple(args)]
    return wrapper
