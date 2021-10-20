class One(object):
    def __init__(self):
        print("One")

class Three(One):
    def __init__(self):
        super(Three,self).__init__()
        print("Three")

class Two(One):
    def __init__(self):
        super(Two,self).__init__()
        print("Two")

class Four(Three):
    def __init__(self):
        super(Four,self).__init__()
        print("Four")

class Final(Four,Two):
    def __init__(self):
        super(Final,self).__init__()
        print("Final")
print(Final.mro())
inst=Final()