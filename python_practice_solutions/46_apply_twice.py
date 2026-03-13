
def apply_twice(func,x):
    return func(func(x))

def square(n): return n*n
print(apply_twice(square,2))
