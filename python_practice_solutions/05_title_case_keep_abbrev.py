
def smart_title(sentence, abbreviations={"AI","ML"}):
    words = sentence.split()
    result = []
    for w in words:
        if w.upper() in abbreviations:
            result.append(w.upper())
        else:
            result.append(w.capitalize())
    return " ".join(result)
