topping_cost = 10 + 2.5
active = True
toppings_list = []

while active:
    toppings = input("Please enter a topping (when done type quit): ")
    if toppings == "quit":
        active = False
    else:
        print("I'll add that topping to your pizza")
        toppings_list.append(toppings)

toppings_total = len(toppings_list) * topping_cost
print(
    f"The cost of all of your toppings will be, your toppings: {toppings_list} x £{topping_cost} equalling £{toppings_total}"
)
