
numbers = [10, 5, 0, 2]

for n in numbers:
    try:
        print(100 / n)
    except ZeroDivisionError:
        print("Cannot divide by zero")
