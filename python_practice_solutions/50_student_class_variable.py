
class Student:
    school_name="ABC School"
    def __init__(self,name,roll):
        self.name=name
        self.roll_no=roll

s1=Student("A",1)
s2=Student("B",2)
Student.school_name="XYZ School"
print(s1.school_name,s2.school_name)
