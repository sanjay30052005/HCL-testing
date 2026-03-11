
def normalize_name(s):
    s=s.strip()
    if not s:
        return ""
    return " ".join(s.split()).title()
