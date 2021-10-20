"""
Create a log decorator with parameters. You can take my_benchmark_decor decorator from day03/fn_decorators.py as basis

Decorator should take 1 parameters - function that converts elapsed time into into string with specific format for example: "00h 00min 01sec 123ms"

"""
import datetime
import time
import functools
def decor_time(format):
    def my_benchmark_decor(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            print("starting function {}".format(fn.__name__))
            res = fn(*args, **kwargs)
            time.sleep(1)
            time_passed = time.gmtime(time.time() - start_time)
            print("function {} finished in {}".format(fn.__name__,time.strftime(format, time_passed)))
            return res
        return wrapper
    return my_benchmark_decor

@decor_time("%H:%M:%S")
def greeting2(greet, name, surname, age):
    print(greet, name, surname, age)



greeting2("Hello", "Tom", "Tomson", 100)