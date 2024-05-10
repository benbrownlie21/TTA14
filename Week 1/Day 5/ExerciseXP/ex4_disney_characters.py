users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# question 1
disney_users_A = {}
for index, user in enumerate(users):
    disney_users_A[user] = index
print(disney_users_A)

# question 2
y = enumerate(users)
print(dict(y))

# question 3
disney_users_C = {}
for index, user in enumerate(sorted(users)):
    disney_users_C[user] = index
print(disney_users_C)

# question 4.1
for letter in users:
    if "i" in letter:
        print(f"Names with an I within it are: {letter}")

# question 4.2
for name in users:
    first_letter = name[0]
    if first_letter == "M" or first_letter == "P":
        print(f"Names starting with an M or P are: {name}")
