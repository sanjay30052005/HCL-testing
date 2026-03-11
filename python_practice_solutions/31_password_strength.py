
def check_strength(pwd, min_len=8):
    return {
        "length_ok": len(pwd)>=min_len,
        "has_upper": any(c.isupper() for c in pwd),
        "has_lower": any(c.islower() for c in pwd),
        "has_digit": any(c.isdigit() for c in pwd),
        "has_special": any(not c.isalnum() for c in pwd),
        "score": sum([
            len(pwd)>=min_len,
            any(c.isupper() for c in pwd),
            any(c.islower() for c in pwd),
            any(c.isdigit() for c in pwd),
            any(not c.isalnum() for c in pwd)
        ])
    }
