
class BankAccount:
    def __init__(self):
        self.__balance=0
    def deposit(self,a): self.__balance+=a
    def withdraw(self,a):
        if a<=self.__balance: self.__balance-=a
    def get_balance(self): return self.__balance

b=BankAccount()
b.deposit(1000)
b.withdraw(200)
print(b.get_balance())
