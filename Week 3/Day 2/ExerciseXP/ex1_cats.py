class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Tom", 14)
cat2 = Cat("Mike", 5)
cat3 = Cat("Leslie", 10)


def oldest_cat(*args):
    return max(args)


print(
    f"The oldest cat is {oldest_cat(cat1.name, cat2.name, cat3.name)} and its age is {oldest_cat(cat1.age, cat2.age, cat3.age)}"
)
