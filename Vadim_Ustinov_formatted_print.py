"""
Task: Create a custom print method 'formated_print' with one mandatory field fmt
that defines resulting string format. Method should accept any number of
optional indexed or name parameters debending on format string defined.

examples:

formated_print("Hello, {0} {1}" , "Jim", "Johnson")
formated_print("{name} is {age} years old" , name="Piotr", age=25)
formated_print("{city} is great for {0}" , "sightseeing", city="Rome")

should print:
>> Hello, Jim Johnson
>> Piotr is 25 years old
>> Rome is great for sightseeing


"""


def formated_print(fmt, *args, **kwargs):
    for kwarg in kwargs:
        fmt=fmt.replace("{"+str(kwarg)+"}",str(kwargs[kwarg]))
    fmt=fmt.format(*args) if args else fmt
    print(fmt)

formated_print("Hello, {0} {1}" , "Jim", "Johnson")
formated_print("{name} is {age} years old" , name="Piotr", age=25)
formated_print("{city} is great for {0}" , "sightseeing", city="Rome")