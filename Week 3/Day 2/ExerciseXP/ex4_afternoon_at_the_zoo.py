class Zoo:

    def __init__(self, _zoo_name):
        self.animals = []
        self.name = _zoo_name

    def add_animal(self, new_animal):
        self.animals.append(new_animal)
        print(f"{new_animal} has been added to the zoo")

    def get_animals(self):
        for animal_name in self.animals:
            print(animal_name)

    def sell_animal(self, animal_sold):
        self.animals.remove(animal_sold)
        print(f"{animal_sold} has been removed from the zoo")

    def sort_animals(self):
        self.animals.sort()
        for animal_name in self.animals:
            print(animal_name)


zoo = Zoo("My Zoo")

zoo.add_animal("Bear")
zoo.add_animal("Snake")
zoo.add_animal("Lion")
zoo.add_animal("Elephant")

zoo.sell_animal("Snake")

zoo.get_animals()
zoo.sort_animals()
