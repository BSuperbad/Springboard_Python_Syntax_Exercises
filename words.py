def print_upper_words(words):
    """Print each word on separate line uppercased"""
    for word in words:
        print(word.upper())


def print_words_e_starting(words):
    """Print each word on separate line if it starts with 'e' or 'E'"""
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word)


def print_words_starting_with(words, must_start_with):
    """Print each word on separate line uppercased if it starts with the character passed in"""
    for word in words:
        for char in must_start_with:
            if word.startswith(char):
                print(word.upper())
