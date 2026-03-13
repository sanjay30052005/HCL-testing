
class Base:
    def __init__(self):
        self._salary=50000
        self.__bonus=5000

class Child(Base):
    def show(self):
        print(self._salary)

Child().show()
