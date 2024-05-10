import random
import string


def random_word(length=5):
    word1 = string.ascii_letters.lower()
    word2 = string.ascii_letters.upper()
    return "".join(
        random.choice(word1) + "".join(random.choice(word2)) for i in range(length)
    )


print(random_word())
