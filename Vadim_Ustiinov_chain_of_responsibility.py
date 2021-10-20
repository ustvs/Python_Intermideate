"""
1. create several classes responsible for one operation each. Let's the operations
be: '+'- sum, '-' - subtraction, '*' - multiplication, '/' - division, '**' - power
2. each class __init__ method should receive and keep one parameter 'next'
that represents next object in the chain of responsibility. Assign a default
value None to the parameter
3. each class should have a method 'run' with one parameter 'operation' that
represents an operation to run.
4. Each class run can fulfil only one type of operation so 'run' should
check 'operation' parameter and execute operation if it's the one. 
If it's an operation that class is not supposed to handle, run should call 
'run' method of the next element in the chain. If 'self.next' is None than
'run' should return None
    5. object that describe the operation should have a type of operation that
    contains one of the values +, -, *, /, ** and the value to apply the
    operation to. Let allow '+' and '*' to accept 2 or more arguments. 
    Try to decide yourself how you implement this operation descriptor object. 
    It can be a separate class or classes, dictionary, list, tuple - it's up to you

"""
def operaton(*argv):
    if argv[0] == '+':
        res= sum(argv[1:])
    if argv[0] == '-':
        res= argv[1]-argv[2]
    if argv[0] == '*':
        res=1
        for i in argv[1:]:
           res *= i 
    if argv[0] == '/':
        res= argv[1]/argv[2]
    if argv[0] == '**':
        res = argv[1] ** argv[2]
    
    return res

class Sum(object):
    next=None
    operation='+'
    def __init__(self, next=None):
        self.next=next
    def run(self,*cmd):
        if cmd[0] == self.operation:
            return operaton(*cmd)
        else:
            if self.next != None:
                return self.next.run(*cmd)
            else:
                return None
class Sub(object):
    next=None
    operation='-'
    def __init__(self, next=None):
        self.next=next
    def run(self,*cmd):
        if cmd[0] == self.operation:
            return operaton(*cmd)
        else:
            if self.next != None:
                return self.next.run(*cmd)
            else:
                return None

class Mlt(object):
    next=None
    operation='*'
    def __init__(self, next=None):
        self.next=next
    def run(self,*cmd):
        if cmd[0] == self.operation:
            return operaton(*cmd)
        else:
            if self.next != None:
                return self.next.run(*cmd)
            else:
                return None

class Div(object):
    next=None
    operation='/'
    def __init__(self, next=None):
        self.next=next
    def run(self,*cmd):
        if cmd[0] == self.operation:
            return operaton(*cmd)
        else:
            if self.next != None:
                return self.next.run(*cmd)
            else:
                return None

class Pow(object):
    next=None
    operation='**'
    def __init__(self, next=None):
        self.next=next
    def run(self,*cmd):
        if cmd[0] == self.operation:
            return operaton(*cmd)
        else:
            if self.next != None:
                return self.next.run(*cmd)
            else:
                return None

op=['**',2,3,3,4,5]
chain=Sub(Sum(Mlt(Div(Pow()))))
print(chain.run(*op))

"""
    7. Optional. think what you have in common in all created operation classes. 
    Try to create a base class and move all common code to it
"""
class co(object):
    next=None
    operation=''
    def __init__(self, operation='', next=None):
        self.next=next
        self.operation=operation
    def run(self,*cmd):
        if cmd[0] == self.operation:
            return operaton(*cmd)
        else:
            if self.next != None:
                return self.next.run(*cmd)
            else:
                return None

chain2=co('-',co('+',co('*',co('/',co('**')))))
print(chain2.run(*op))