
from abc import ABC, abstractmethod

class Validator(ABC):
    @abstractmethod
    def validate(self, data):
        pass

class EmailValidator(Validator):
    def validate(self, data):
        return "@" in data

class PasswordValidator(Validator):
    def validate(self, data):
        return len(data) >= 8

print(EmailValidator().validate("test@gmail.com"))
print(PasswordValidator().validate("secret123"))
