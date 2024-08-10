from faker import Faker

fake = Faker()


def user_data():
    users = {}
    for i in range(0, 10):
        users[i] = {}
        users[i]["Name"] = fake.name()
        users[i]["Address"] = fake.address()
        users[i]["Language"] = fake.language_code()
    print(users)


user_data()
