"""
Create several ariphmetical functions like sum, sub, mult and div, each should take 2 parameters and return a result of the operation

Create a decorator that would check parameters of called decorated function to be integers.
If any of parameters is not int print an error message and return None, if all parameters are integers call decorated function
"""

def check_parameter_types_are_ints(fn):
    def inner(x,y):
        if isinstance(x,(int,float)) and isinstance(y,(int,float)):
            if fn == div:
                if y == 0:
                    print("Divide by 0!")
                    return None
            else:
                return fn(x,y)
        else:
            print("No number used")
            return None
    return inner

@check_parameter_types_are_ints
def sum(x,y):
    return x+y
@check_parameter_types_are_ints
def sub(x,y):
    return x-y
@check_parameter_types_are_ints
def mult(x,y):
    return x*y
@check_parameter_types_are_ints
def div(x,y):
    return x/y


print (sum(2,3))


a = 10
b = 2
print("{} + {} = {}".format(a, b , sum(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
print("{} * {} = {}".format(a, b, mult(a, b)))

a = "ten"
b = "two"
print("{} + {} = {}".format(a, b , sum(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
print("{} * {} = {}".format(a, b, mult(a, b)))
