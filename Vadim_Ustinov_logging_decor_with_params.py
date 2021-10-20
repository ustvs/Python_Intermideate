"""
Create a log decorator with parameters. You can take my_logging_decor decorator from day03/fn_decorators.py as basis
Decorator should take 2 parameters - format strings for messages printed before and after decorated function call
"""
import functools

def log_format(format_start,format_end):
    def my_logging_decor(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print(format_start.format(fn.__name__))
            res = fn(*args, **kwargs)
            print(format_end.format(fn.__name__))
            return res 
    
        return wrapper
    return my_logging_decor

@log_format("Start of {}","End of {}")
def say_w(w):
    print(w)

say_w("W")
