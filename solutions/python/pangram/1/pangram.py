def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence_letters = set(sentence.lower());
    return alphabet.issubset(sentence_letters);