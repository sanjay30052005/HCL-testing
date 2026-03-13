
from abc import ABC,abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self): pass
    @abstractmethod
    def refund(self): pass

class CreditCardPayment(PaymentGateway):
    def pay(self): print("Card pay")
    def refund(self): print("Card refund")
