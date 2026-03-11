
def running_max_reset(lst):
    result=[]
    current=0
    for x in lst:
        if x<=0:
            current=0
        else:
            current=max(current,x)
        result.append(current)
    return result
