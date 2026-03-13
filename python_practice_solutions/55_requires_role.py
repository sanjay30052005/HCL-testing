
class User:
    def __init__(self,role): self.role=role

current_user=User("admin")

def requires_role(role):
    def dec(fn):
        def wrap(*a,**k):
            if current_user.role!=role:
                raise PermissionError("Denied")
            return fn(*a,**k)
        return wrap
    return dec

@requires_role("admin")
def delete():
    print("Deleted")

delete()
