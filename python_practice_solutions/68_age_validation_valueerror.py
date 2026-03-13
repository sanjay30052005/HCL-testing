
def validate_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    return "Valid age"

print(validate_age(20))
