
class Writer:
    def write(self): print("Writing")

class Reader:
    def read(self): print("Reading")

class Editor(Writer,Reader): pass

e=Editor()
e.write()
e.read()
