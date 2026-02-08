def is_valid(isbn):
    # Clean the input: keep only alphanumeric characters
    cleaned = ''.join(c for c in isbn if c.isalnum())
    
    # Length must be exactly 10
    if len(cleaned) != 10:
        return False
    
    # Check if all characters except last are digits
    if not all(c.isdigit() for c in cleaned[:-1]):
        return False
    
    # Last character must be digit or 'X'
    if cleaned[-1] not in '0123456789X':
        return False
    
    # Calculate weighted sum
    total = 0
    for i, c in enumerate(cleaned):
        if i == 9 and c == 'X':
            total += 10 * 1
        elif c.isdigit():
            total += int(c) * (10 - i)
        else:
            return False
    
    # Check if divisible by 11
    return total % 11 == 0