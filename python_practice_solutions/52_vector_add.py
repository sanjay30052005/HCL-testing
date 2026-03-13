
class Vector:
    def __init__(self,x,y):
        self.x=x; self.y=y
    def __add__(self,o):
        return Vector(self.x+o.x,self.y+o.y)
    def __repr__(self):
        return f"Vector({self.x},{self.y})"

print(Vector(1,2)+Vector(3,4))
