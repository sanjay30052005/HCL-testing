
def cumulative_until_negative(lst):
    total=0
    result=[]
    for x in lst:
        if x<0:
            break
        total+=x
        result.append(total)
    return result
