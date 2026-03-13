
def make_accumulator(start=0):
    total=start
    def add(v):
        nonlocal total
        total+=v
        return total
    return add

acc=make_accumulator()
print(acc(5),acc(10))
