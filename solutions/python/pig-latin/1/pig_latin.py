def translate(text):
    return ' '.join(translate_word(word) for word in text.split())

def translate_word(word):
    vowels = 'aeiou'
    
    # Rule 1: starts with vowel, "xr", or "yt"
    if word in vowels or word.startswith(('xr', 'yt')):
        return word + 'ay'
    
    # Rule 3: consonants (0+) followed by "qu" (no vowel before)
    qu_index = word.find('qu')
    if qu_index != -1 and qu_index < len(word) - 2 and not any(c in vowels for c in word[:qu_index]):
        return word[qu_index + 2:] + word[:qu_index + 2] + 'ay'
    
    # Rule 4: consonants followed by "y" (before any vowel)
    for i in range(1, len(word)):
        if word[i] == 'y' and not any(c in vowels for c in word[:i]): 
            return word[i:] + word[:i] + 'ay'
    
    # Rule 2: starts with consonants
    for i, char in enumerate(word):
        if char in vowels:
            return word[i:] + word[:i] + 'ay'
    
    return word + 'ay'