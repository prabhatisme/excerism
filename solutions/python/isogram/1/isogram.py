def is_isogram(string):
    seen = set()
    for c in string.lower():
        if c in ' -':
            continue
        if c in seen:
            return False
        seen.add(c)
    return True