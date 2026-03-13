
with open("log.txt") as f:
    text = f.read()

print("ERROR count:", text.count("ERROR"))
