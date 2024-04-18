class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        return f"{self.name} goes woof!"

    def jump(self):
        x = self.height * 2
        return f"{self.name} jumps {x}cm high!"


davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)


print(
    f"David's dog is called {davids_dog.name}, and he is {davids_dog.height}cm tall. {davids_dog.bark()}. {davids_dog.jump()}"
)

print(
    f"Sarah's dog is called {sarahs_dog.name}, and he is {sarahs_dog.height}cm tall. {sarahs_dog.bark()}. {sarahs_dog.jump()}"
)
