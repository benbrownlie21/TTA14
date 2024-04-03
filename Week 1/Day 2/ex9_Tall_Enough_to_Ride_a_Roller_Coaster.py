# Write code that will ask the user for their height in centimeters.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

your_height = int(input("Please enter your height in centimeters: ") + "cm")
needed_height = 145

if your_height > needed_height:
    print("You are tall enough to ride this roller coaster, have fun!")
elif your_height == needed_height:
    print(
        f"You have made the needed height of {needed_height}, but you should really grow some more!"
    )
else:
    print(
        f"Sorry you aren't tall enough to ride the roller coaster, you have to be at least {needed_height}cm and you are {your_height}cm. If you grow come back!"
    )
