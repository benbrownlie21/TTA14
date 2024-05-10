user_favourite_fruits = input("Please enter your favourite fruit(s): ")
favourite_fruits_list = [fruit.strip() for fruit in user_favourite_fruits.split(",")]

while True:
    new_list = input("Input a name of a fruit: ")
    if new_list in favourite_fruits_list:
        print("You chose one of your favorite fruits! Enjoy!")
        break
    else:
        print("You chose a new fruit. I hope you enjoy")
        break
