
def password_check(correct_pwd):
    for _ in range(3):
        pwd = input("Enter password: ")
        if pwd == correct_pwd:
            return "Unlocked"
    return "Locked"
