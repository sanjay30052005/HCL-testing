
def counter():
    c=0
    def next():
        nonlocal c
        c+=1
        return c
    return next

n=counter()
print(n(),n(),n())
