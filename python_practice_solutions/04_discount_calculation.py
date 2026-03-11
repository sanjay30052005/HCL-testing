
def final_payable(amount):
    if amount < 1000:
        discount = 0
    elif amount < 5000:
        discount = 0.05
    else:
        discount = 0.10
    return amount * (1 - discount)
