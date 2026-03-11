
def second_largest_index(lst):
    unique=sorted(set(lst), reverse=True)
    if len(unique)<2:
        return -1
    val=unique[1]
    return lst.index(val)
