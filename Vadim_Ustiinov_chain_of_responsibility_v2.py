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
     operation='+'
     def __init__(self):
        if command[0] == Sum.operation:
            return operaton(*command)
        else:
            return(super(Sum,self).__init__())

class Sub(object):
    operation='-'
    def __init__(self):
        if command[0] == Sub.operation:
            return operaton(*command)
        else:
            return(super(Sub,self).__init__())

class Mlt(object):
    operation='*'
    def __init__(self):
        if command[0] == Mlt.operation:
            return operaton(*command)
        else:
            return(super(Mlt,self).__init__())

class Div(object):
    operation='/'
    def __init__(self):
        if command[0] == Div.operation:
            return operaton(*command)
        else:
            return(super(Div,self).__init__())

class Pow(object):
    operation='**'
    def __init__(self):
        if command[0] == Pow.operation:
            return operaton(*command)
        else:
            return(super(Pow,self).__init__())

command=['+',2,3,3,4,5]

class Chain(Pow,Mlt,Div,Sum):
    def __init__(self):
        cmd=command
        print(super(Chain,self).__init__())

print(Chain.mro())
chain = Chain()
