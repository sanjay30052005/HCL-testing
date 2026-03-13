
card = "1234567812345678"
masked = "*" * (len(card) - 4) + card[-4:]
print(masked)
