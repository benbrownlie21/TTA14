import random

user_input = str(
    input("Please enter a string (it must be more than 10 characters long): ")
)
first_letter = user_input[0]
last_letter = user_input[-1]

if len(user_input) < 10:
    print("The string is not long enough")
elif len(user_input) > 10:
    print("The string is too long")
else:
    print("Perfect string!")

print(
    f"The first letter of your string is: {first_letter}, and the last letter is: {last_letter}"
)


my_word = "This is a new world"
words = list(my_word)
random.shuffle(words)
shuffled_words = "".join(words)
print(shuffled_words)
