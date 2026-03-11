
def remove_keep_last(lst):
    seen=set()
    result=[]
    for item in reversed(lst):
        if item not in seen:
            seen.add(item)
            result.append(item)
    return list(reversed(result))
