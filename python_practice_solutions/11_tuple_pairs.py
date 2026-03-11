
def to_pairs(lst):
    return [(lst[i], lst[i+1]) for i in range(0,len(lst)-1,2)]
