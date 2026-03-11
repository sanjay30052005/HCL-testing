
def rotate_right(lst, k):
    n=len(lst)
    k%=n
    for _ in range(k):
        lst.insert(0,lst.pop())
    return lst
