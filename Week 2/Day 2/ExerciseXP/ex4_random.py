from random import randint

print(randint(3, 9))

your_number = int(input("Enter a number between 1 and 100: "))
my_number = randint(0, 100)


def random_number(your_number, my_number):
    if your_number == my_number:
        print("You chose the same number as I did! CONGRATS!!")
    else:
        print("Your number was different to mine, uh oh!")
    print(f"Your number: {your_number}\nMy number: {my_number}")


random_number(your_number, my_number)
