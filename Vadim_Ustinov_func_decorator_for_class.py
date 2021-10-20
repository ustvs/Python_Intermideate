import functools
def TypeControl(cls):
 
    def __any_getter(self, prop_name):
        print(f"getting {prop_name}")
        return getattr(self, prop_name)

    def __any_setter(self, value, prop_name, prop_type):
        print(f"setting {prop_name} to {value}")
        if isinstance(value,prop_type):
            setattr(self, prop_name, value)
        else:
            print(f"{prop_name} has the wrong type {type(value)} and has to be {prop_type}")

            
    cls.nameType = cls.name
    del cls.name
    cls.name = property(
    functools.partial(__any_getter, prop_name="__name"), 
    functools.partial(__any_setter, prop_name="__name",prop_type=cls.nameType))

    cls.surnameType = cls.surname
    del cls.surname
    cls.surname = property(
    functools.partial(__any_getter, prop_name="__surname"), 
    functools.partial(__any_setter, prop_name="__surname",prop_type=cls.surnameType))

    cls.ageType = cls.age
    del cls.age
    cls.age = property(
    functools.partial(__any_getter, prop_name="__age"), 
    functools.partial(__any_setter, prop_name="__age",prop_type=cls.ageType))

    cls.salaryType = cls.salary
    del cls.salary
    cls.salary = property(
    functools.partial(__any_getter, prop_name="__salary"), 
    functools.partial(__any_setter, prop_name="__salary",prop_type=cls.salaryType))

    return cls

@TypeControl
class MyClass:
    def __init__(self, name, surname, age, salary):
        self.name=name
        self.surname=surname
        self.age=age
        self.salary=salary
    def showMe(self):
        print(f"{self.name} {self.surname} is {self.age} years old and have the salary of {self.salary}$")    
    name = str
    surname = str
    age = int
    salary = float

person = MyClass("Tom", "Johnson", 25, 500.00)
person.showMe()
