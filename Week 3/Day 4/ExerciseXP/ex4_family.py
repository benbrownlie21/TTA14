class Family:

    def __init__(self):
        self.members = [
    {"Name": "Sarah", "Age": 46, "Gender": "Female"},
    {"Name": "Tony", "Age": 48, "Gender": "Male"},
    {"Name": "Rachael", "Age": 24, "Gender": "Female"},
    {"Name": "Sam", "Age": 22, "Gender": "Male"},
    {"Name": "Kate", "Age": 5, "Gender": "Female"}
]


    def born(self, **new_member):
        self.members.append(new_member)
        print(f"Congratulations on your new baby {new_member["Name"].upper()}!")

    def is_18(self):
        for member in self.members:
            if member["Age"] > 18:
                member["is_child"] = False
            else:
                member["is_child"] = True

    def family_presentation(self):
        for member in self.members:
            print(f"{member["Name"]} {last_name}")


# members = [
#     {"Name": "Sarah", "Age": 46, "Gender": "Female"},
#     {"Name": "Tony", "Age": 48, "Gender": "Male"},
#     {"Name": "Rachael", "Age": 24, "Gender": "Female"},
#     {"Name": "Sam", "Age": 22, "Gender": "Male"},
#     {"Name": "Kate", "Age": 5, "Gender": "Female"}
# ]

family = Family()
last_name = "Smith"
family.born(Name="Sophia", Age=0, Gender="Female")
family.family_presentation()
family.is_18()

print(family.members)
