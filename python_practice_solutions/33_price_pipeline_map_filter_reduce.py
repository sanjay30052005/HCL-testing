
from functools import reduce
def final_bill(prices):
    discounted = map(lambda p: p*0.9, prices)
    filtered = filter(lambda p: p>=200, discounted)
    return reduce(lambda a,b: a+b, filtered, 0)
