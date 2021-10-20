class UniqueIterator:
    words={''}
    line=[]
    index=0
    def __init__(self, file):
        with open(file,"r") as source:
            self.text=source.readlines()
        self.index=0
    
    def __iter__(self):
        self.index=0
        return self
    
    def __next__(self):
        while True:    
            line=self.text[self.index].split()
            for i in line:
                if i in self.words:
                    continue
                else:
                    self.words.add(i)
                    return i
            if (self.index+1) < len(self.text):
                self.index +=1
            else:
                raise StopIteration() 


U=UniqueIterator("Raven.txt")
for i in U:
    print(i)
