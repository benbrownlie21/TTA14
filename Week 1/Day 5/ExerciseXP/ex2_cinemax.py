family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

prices_per_age = {}
for name, age in family.items():
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    prices_per_age[age] = price
    print(f"The price per person is: {name.capitalize()} --> £{price}\n")

tickets_total = sum(prices_per_age.values())
print(f"The total cost of the families tickets will be £{tickets_total}")
