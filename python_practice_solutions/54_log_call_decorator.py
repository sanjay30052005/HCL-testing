
from functools import wraps

def log_call(fn):
    @wraps(fn)
    def wrapper(*a,**k):
        print("Calling",fn.__name__,a)
        r=fn(*a,**k)
        print("Return",r)
        return r
    return wrapper

@log_call
def add(a,b): return a+b

add(3,4)
