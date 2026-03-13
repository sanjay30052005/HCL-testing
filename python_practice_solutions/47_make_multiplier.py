
def make_multiplier(k):
    def mul(x): return x*k
    return mul

double=make_multiplier(2)
print(double(5))
