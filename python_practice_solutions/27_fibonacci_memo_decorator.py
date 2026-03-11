
def memoize(fn):
    cache={}
    def wrapper(n):
        if n not in cache:
            cache[n]=fn(n)
        return cache[n]
    return wrapper

@memoize
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
