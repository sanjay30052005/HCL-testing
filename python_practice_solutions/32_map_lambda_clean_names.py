
names = ["  alpha Case  ", "Beta   unit", "gAmMa MODULE  "]
clean = list(map(lambda x: " ".join(x.strip().split()).title(), names))
print(clean)
