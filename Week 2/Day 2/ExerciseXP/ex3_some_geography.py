city = input("Please write the city you live in: ")
country = input("Please write the country you live in: ")


def describe_city(city, country):
    if city and country:
        print(f"{city.capitalize()} is in {country.capitalize()}")
    else:
        print("London is in the UK")


describe_city(city, country)
