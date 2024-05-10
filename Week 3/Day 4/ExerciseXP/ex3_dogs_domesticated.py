from ex2_dogs import Dog, dog_1, dog_2, dog_3
import random


class PetDog(Dog):
    def __init__(self, all_dogs):
        self.all_dogs = all_dogs
        self.trained_f = False

    def trained(self):
        print(Dog.bark)
        self.trained_f = True

    def play(self, *dogs):
        dog_names = [dog.name for dog in dogs]
        print(", ".join(dog_names) + " all play together")

    def do_a_trick(self):
        trick = random.choice(all_tricks)
        if self.trained_f == True:
            for dog in self.all_dogs:
                print(f"{dog.name} {trick}")
        else:
            for dog in self.all_dogs:
                print(f"{dog.name} plays dead")


all_dogs = [dog_1, dog_2, dog_3]
pet_dog = PetDog(all_dogs)
pet_dog.play(*all_dogs)
trick_1 = "does a barrel roll"
trick_2 = "stands on its back legs"
trick_3 = "shakes your hand"
all_tricks = [trick_1, trick_2, trick_3]
pet_dog.do_a_trick()
