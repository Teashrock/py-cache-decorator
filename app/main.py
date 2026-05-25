from typing import Callable, Any
from functools import wraps

cache_dict = {}


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = func.__name__, args, tuple(sorted(kwargs.items()))
        if key not in cache_dict:
            print("Calculating new result")
            cache_dict[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_dict[key]
    return wrapper
    
# @cache
# def long_time_func(a, b, c):
#     return (a ** b ** c) % (a * c)

# @cache
# def long_time_func_2(text_1, text_2):
#     return f"{text_1.upper()}, {text_2.lower()}"

# @cache
# def long_time_func_3(n_list, text):
#     return f"{[i ** 2 for i in n_list]}, {text}"

# long_time_func(1, 2, 3)
# long_time_func(1, 2, 3)
# long_time_func(1, 2, 3)
# long_time_func_3((10, 20, 30), "wow, numbers!")
# long_time_func(2, 2, 3)
# long_time_func_2("Hello", "world")
# long_time_func(1, 2, 3)
# long_time_func_2("Hello", "Mark")
# long_time_func_2("Hello", "Mark")
# long_time_func_3((10, 20, 30), "wow, numbers!")
# long_time_func_3((10, 20, 30), "egh, numbers...")