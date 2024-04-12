shirt_size = input("What is your shirt size (S, M, L): ")
shirt_message = input("What do you want printed on your shirt: ")


def make_shirt(shirt_size="L", shirt_message="I love Python"):
    print(
        f"You chose the shirt size of {shirt_size.upper()}, and the message to be printed on your shirt is: '{shirt_message}'."
    )
    if shirt_size == "L":
        print("This is a Large shirt")
    elif shirt_size == "M":
        print("This is a Medium shirt")
    elif shirt_size == "S":
        print("This is a Small shirt")
    else:
        print("This is not a real size!")


make_shirt(shirt_size, shirt_message)
