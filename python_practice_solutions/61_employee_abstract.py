
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000

class Intern(Employee):
    def calculate_salary(self):
        return 10000

e1 = FullTimeEmployee("Alice", 1)
e2 = Intern("Bob", 2)

print(e1.name, e1.calculate_salary())
print(e2.name, e2.calculate_salary())
