from ex4_family import Family, last_name

class TheIncredibles(Family):

    def powers_and_name(self, **new_power_and_name):
        self.members.append(new_power_and_name)

    def use_power(self):
        for member in self.members:
            if member["Age"] > 18:
                print(f"{member["Name"]} - {member["power"]}")
            else:
                raise Exception("Not powers under 18")
            
    def incredible_presentation(self):
        for member in self.members:
            power = member.get("power", "No Power")
            super_name = member.get("super_name", "Unknown")
            print(f"This is our incredible family!: \n{last_name} - {member["Name"]}, {member["Age"]}, {member["Gender"]}, {power}, {super_name}")



incredibles_family = TheIncredibles()
incredibles_family.powers_and_name(Name= "Sarah", Age= 46, Gender= "Female", power= "Invisibility", super_name= "Wonder Woman")
incredibles_family.powers_and_name(Name= "Tony", Age= 48, Gender= "Male", power= "Super Speed", super_name= "Super Man")
incredibles_family.powers_and_name(Name= "Rachael", Age= 24, Gender= "Female", power= "Super Strength", super_name= "Super Woman")
incredibles_family.powers_and_name(Name= "Sam", Age= 22, Gender= "Male", power= "Fire", super_name= "Spiderman")
incredibles_family.powers_and_name(Name= "Kate", Age= 5, Gender= "Female", power= "Mind Reading", super_name= "Agent X")

incredibles_family.incredible_presentation()
incredibles_family.born(Name="Baby Jack", Age=0, Gender="Male", power="Unknown Power", super_name="Unknown")
incredibles_family.incredible_presentation()
