# this is variable for a user to enter the first name and is a string
first_name = input("Please enter your first name: ").capitalize()

# this is variable for a user to enter the first name and is a string
last_name = input("Please enter your last name: ").capitalize()

# this is a variable for age stored as int
age = int(input("Please enter your age: "))

# this is a variable of the users age stored as string
gender = input("Please enter your gender: ").capitalize()

# this is a variable of the users email stored as string
email = input("Please enter your email address: ")

# this is a variable of the users password stored as string
password = input("Please enter your password: ")

print(
    f"""Hi {first_name} {last_name}, below are the details of your new account: 
    \n - You are {age} years old
    \n - Your saved gender is: {gender}
    \n - Your account has the email address {email} and you chose the password is: {password}"""
)
