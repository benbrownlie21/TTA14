import random


class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self._id_number = str(id_number)
        self._name = str(name)
        self._age = int(age)
        self._priority = bool(priority)
        self._blood_type = str(blood_type)


class Family:
    def __init__(self):
        self.family = []

    def add_family_member(self, person):
        self.family.append(person)
        print(f"{person._name} has been added to the family")


class Queue:
    def __init__(self):
        self.persons = []

    def add_person(self, person):
        if person._age >= 60:
            self.persons.insert(0, person)
        else:
            self.persons.append(person)
        print(f"{person._name} has been added to the queue")

    def find_in_queue(self, name):
        for index, person in enumerate(self.persons):
            if person._name == name:
                print(f"{person._name} is number {index + 1} in the queue")
                return
        else:
            print(f"{name} is not in the queue")

    def queue_list(self):
        for person in self.persons:
            print(
                f"Name: {person._name}, Age: {person._age}, Priority: {person._priority}, Blood Type: {person._blood_type}"
            )

    def swap(self, person1, person2):
        if 0 <= person1 < len(self.persons) and 0 <= person2 < len(self.persons):
            self.persons[person1], self.persons[person2] = (
                self.persons[person2],
                self.persons[person1],
            )
            print(
                f"{self.persons[person1]._name} and {self.persons[person2]._name} have switched positions"
            )
        else:
            print("Invalid")

    def get_next(self):
        if self.persons:
            person = self.persons[0]
            print(
                f"NEXT IN LINE IS:: Name: {person._name}, Age: {person._age}, Priority: {person._priority}, Blood Type: {person._blood_type}"
            )
        else:
            print("No records here")

    def get_next_blood_type(self):
        blood_type = "AB"
        found = False
        for person in self.persons:
            if person._blood_type == blood_type:
                found = True
                print(
                    f"Name: {person._name}, Age: {person._age}, Priority: {person._priority}, Blood Type: {person._blood_type}"
                )
                break
        if not found:
            print(f"No patients Blood Type {self.blood_type}")

    def sort_by_age(self):
        n = len(self.persons)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.persons[j]._age < self.persons[j + 1]._age:
                    self.persons[j], self.persons[j + 1] = (
                        self.persons[j + 1],
                        self.persons[j],
                    )
        for person in self.persons:
            print(f"Name: {person._name}, Age: {person._age}")

    def rearrange_queue(self):
        for i in range(len(self.persons)):
            for j in range(i + 1, len(self.persons)):
                if self.persons[i]._id_number == self.persons[j]._id_number:
                    random.shuffle(self.queue_list)
                    return self.queue_list


queue = Queue()
person1 = Human(1, "Thomas", 38, False, "A")
person2 = Human(2, "Rachel", 24, True, "AB")
person3 = Human(3, "Samantha", 68, False, "O")
person4 = Human(4, "Bob", 82, True, "AB")
queue.add_person(person1)
queue.add_person(person2)
queue.add_person(person3)
queue.add_person(person4)

search = input("\nWhat is the name of the person you want to search for: ")
queue.find_in_queue(search)

queue.queue_list()
queue.swap(2, 3)
queue.sort_by_age()
queue.get_next()
queue.get_next_blood_type()

family = Family()
family1 = Human(1, "Richard", 38, False, "A")
family2 = Human(2, "Sarah", 36, True, "AB")
family3 = Human(3, "Emma", 10, False, "O")
family4 = Human(4, "George", 8, True, "AB")
family.add_family_member(family1)
family.add_family_member(family2)
family.add_family_member(family3)
family.add_family_member(family4)

queue.rearrange_queue()
