
def merge_inventory(a,b):
    result=a.copy()
    for k,v in b.items():
        result[k]=result.get(k,0)+v
    return result
