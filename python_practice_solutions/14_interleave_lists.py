
def interleave(a,b):
    return [val for pair in zip(a,b) for val in pair]
