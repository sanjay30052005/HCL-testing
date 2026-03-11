
def count_overlapping(text, sub):
    count = 0
    for i in range(len(text) - len(sub) + 1):
        if text[i:i+len(sub)] == sub:
            count += 1
    return count
