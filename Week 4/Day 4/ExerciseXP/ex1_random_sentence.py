import random


def get_words_from_file():
    lines = None
    with open("./Week 4/Day 4/ExerciseXP/word_list.txt", "r") as file:
        lines = file.readlines()

    words_list = [word.strip() for line in lines for word in line.split()]
    return words_list


def get_random_sentence(words_list, length):
    random_sentence = " ".join(random.choices(words_list, k=length))
    return random_sentence


def main():
    print("This program shows the user a random sentence")
    words_list = get_words_from_file()
    user_input = input("Choose a length: ")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Not a number")
        return
    random_sentence = get_random_sentence(words_list, user_input)
    print(random_sentence)


if __name__ == "__main__":
    main()
