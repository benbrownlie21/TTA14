from anagram_checker import AnagramChecker


def user_menu():
    while True:
        user_input = input("\n--MENU--\n(i) Input word\n(x) Quit\nCHOICE: ")
        return user_input


def main():
    users_choice = user_menu()
    while users_choice != "x":
        new_anagram = AnagramChecker()
        if users_choice == "i":
            user_word = input("Enter a word: ")
            try:
                new_anagram.is_valid_word(user_word)
            except ValueError as e:
                print("Error: ", e)
        users_choice = user_menu()


if __name__ == "__main__":
    main()
