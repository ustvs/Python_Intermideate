import sys
class MyStdoutRedirectContextManager:
    def __init__(self, filename):
        try:
             self.file = open(filename, "a")
             self.opened=True
        except: # IOError:
            self.opened=False
            self.file=sys.stdout
    def __enter__(self):
            if self.opened:
                sys.stdout=self.file
            return self
    def __exit__(self, *argv):
        sys.stdout=sys.__stdout__
        if self.opened:
            self.file.close()
with MyStdoutRedirectContextManager("test"):
    print (f"Test output")

