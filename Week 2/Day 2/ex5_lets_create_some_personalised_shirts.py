shirt_size = input("What is your shirt size (S, M, L): ")
shirt_message = input("What do you want printed on your shirt: ")


def make_shirt(shirt_size, shirt_message):
    print(
        f"You chose the shirt size of {shirt_size.upper()}, and the message to be printed on your shirt is: {shirt_message}"
    )


make_shirt(shirt_size, shirt_message)
