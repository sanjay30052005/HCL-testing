
with open("sample.txt") as f:
    text = f.read()

text = text.replace("Python", "Java")

with open("sample.txt", "w") as f:
    f.write(text)
