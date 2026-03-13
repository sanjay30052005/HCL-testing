
class Vehicle:
    def start(self): print("Start")

class Car(Vehicle):
    def drive(self): print("Drive")

class ElectricCar(Car):
    def charge(self): print("Charge")

e=ElectricCar()
e.start(); e.drive(); e.charge()
