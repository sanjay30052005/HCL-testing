
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Email must contain @")
    return True

validate_email("testexample.com")
