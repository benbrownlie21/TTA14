from datetime import datetime

retirement_age = {"m": 67, "f": 62}
today = datetime.now()
current_year = today.year


def get_age():
    dob = input(f"Please enter your date of birthdate (YYYY-MM-DD): ")
    return dob


year = 1990
month = 4
day = 21

dob = get_age(year, month, day)
dob_date = datetime.strptime(dob, "%Y-%m-%d")
age = (
    today.year
    - dob_date.year
    - ((today.month, today.day) < (dob_date.month, dob_date.day))
)

print(age)


def can_retire(gender, age, years_to_retirement):
    if gender == "M" and age < int(retirement_age["m"]):
        print(f"You are too young to retire, men retire at { int(retirement_age["m"])}, you have {years_to_retirement} years to go")
    elif gender == "M" and age >  int(retirement_age["m"]):
        print("You are over retirement age, stop working!")
    elif gender == "M" and age ==  int(retirement_age["m"]):
        print("You have reached retirement age!!")
    elif gender == "F" and age <  int(retirement_age["f"]):
        print(
            f"You are too young to retire, women retire at {int(retirement_age["f"])}, you have {years_to_retirement} years to go"
        )
    elif gender == "F" and age >  int(retirement_age["f"]):
        print("You are over retirement age, stop working!")
    elif gender == "F" and age ==  int(retirement_age["f"]):
        print("You have reached retirement age!!")
    else:
        print("Keep trying")


gender = input("What is your gender (M or F)? ").upper()
year_to_retirement = int(retirement_age[gender.lower()]) - age

can_retire(gender, age, year_to_retirement)
