ages_input = input("Please enter the ages of each person that needs a ticket: ")
persons_ages = [int(age.strip(", ")) for age in ages_input.split()]


prices_per_age = {}
for age in persons_ages:
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    prices_per_age[age] = price

tickets_total = sum(prices_per_age.values())
print(f"The total cost of your tickets will be £{tickets_total}")
