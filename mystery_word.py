with open('words.txt') as file:
    # words = []
    # for line in file.readlines():
    #     words.append(line.strip())
    words = [line.strip() for line in file.readlines()]

easy_words = []
medium_words = []
hard_words = []
for word in words:
    if len(word) >= 4 and len(word) <= 6:
        easy_words.append(word)

    if len(word) >= 6 and len(word) <= 8:
        medium_words.append(word)

    if len(word) >= 8 and len(word) <= 12:
        hard_words.append(word)


def get_difficulty():
    """Ask user for level of difficulty (easy, medium, hard).
    If they give a bad answer, keep asking them."""

    while True:
        difficulty = input("Enter difficulty (easy, medium, or hard): ")
        if difficulty in ['easy', 'medium', 'hard']:
            return difficulty


def get_difficulty_recursive():
    """Ask user for level of difficulty (easy, medium, hard).
    If they give a bad answer, keep asking them.
    
    Don't do this one -- recursive.
    """

    difficulty = input("Enter difficulty (easy, medium, or hard): ")
    if difficulty in ['easy', 'medium', 'hard']:
        return difficulty

    return get_difficulty_recursive()


def filter_words_by_difficulty(words, difficulty):
    """
    Given a list of words and a difficulty, filter
    that list to the words that are the right length for
    that difficulty and return the filtered list.
    """
    if difficulty == 'easy':
        min_len = 4
        max_len = 6
    elif difficulty == 'medium':
        min_len = 6
        max_len = 8
    else:
        min_len = 8
        max_len = 45

    return [
        word  # collect word
        for word in words  # iterate over words
        # select only words of a certain length
        if len(word) >= min_len and len(word) <= max_len
    ]


print(len(words))
print(words[:10])
