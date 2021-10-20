"""
Create you own version of map function. It should receive 1 mandatory parameter - func, which is python function, and any (zero or more) number of 
optional parameters representing input lists of values. 

function "func" should have as many parameters as you plan to have lists in map function call and return some value calculated based on input parameters

map should have a list as return value, where each element of the list is there result of "func" function applied to values of input list with same index.
map should go through the input lists until reaches end of the shortest one

so if you have function func(a, b c) and 3 lists of values [1,2,3] [4, 5, 6], [7, 8, 9], the result of
map(func, [1,2,3] [4, 5, 6], [7, 8, 9])
should be 

[func(1, 4, 7), func(2, 5, 8), func(3, 6, 9)]

if for example your "func" will just sum the values, the result supposed to be:

[12, 15, 18]
"""
def func(*argv):
    res=0
    for number in argv:
        res += number
    return res

def map(f, *args):
    mapped=[]
    size=len(args[0])
    for arg in args:
        if len(arg) < size:
            size=len(arg)
    for i in range(size):
        arg_i=[]
        for arg in args:
            arg_i.append(arg[i])
        mapped.append(f(*arg_i))

    return mapped

print(map(func, [1,2,3,4],[4,5,6],[7,8,9]))