import random


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.speed = self.weight / self.age * 10

    def bark(self):
        print(f"{self.name} is barking")

    def run_speed(self):
        print(f"The run speed of {self.name} is {round(self.speed, 2)}mph")

    def fight(self):
        first_dog = random.choice(all_dogs)
        first_dog_f = self.speed * self.weight
        other_dog = random.choice(all_dogs)
        other_dog_f = other_dog.speed * other_dog.weight
        if first_dog_f > other_dog_f:
            print(f"{first_dog.name} won! {other_dog.name} lost :-(")
        if first_dog_f < other_dog_f:
            print(f"{other_dog.name} won! {first_dog.name} lost :-(")
        else:
            print(f"{first_dog.name} and {other_dog.name} tied!")


dog_1 = Dog("Rex", 4, 12)
dog_2 = Dog("Mitch", 7, 14)
dog_3 = Dog("Poppy", 13, 8)

all_dogs = [dog_1, dog_2, dog_3]
# other_dog = random.choice(all_dogs)

for dog in all_dogs:
    dog.bark()
    dog.run_speed()
    dog.fight()
