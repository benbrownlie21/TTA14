class AnagramChecker:
    def __init__(self):
        self.file = open("./Week 4/Day 5/sowpods.txt")
        self.words_list = [word.lower() for line in self.file for word in line.split()]

    def is_valid_word(self, word):
        self.word = word.lower()
        if self.word not in self.words_list:
            raise ValueError(f"'{word}' is not a valid word")
        elif not self.word.isalpha:
            raise ValueError(f"'{word}' is not a valid word")
        else:
            print(f"\nYOUR WORD: '{word.upper()}'")
            print("This is a valid English word")

    # def is_anagram(word1, word2):
    #     word1_list = list(word1)
    #     word1_list.sort()
    #     word2_list = list(word2)
    #     word2_list.sort()
    #     return sorted(word1) == sorted(word2)


anagram = AnagramChecker()
try:
    user_word = input("Enter a word: ")
    anagram.is_valid_word(user_word)
except ValueError as e:
    print("Error:", e)

# anagram.is_anagram(word1="robot")
# anagram.is_anagram(word2="tea")
