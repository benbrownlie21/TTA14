brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": {"Amancio", "Ortega", "Gaona"},
    "type_of_clothes": ("men", "women", "children", "home"),
    "international_competitors": ("Gap", "H&M", "Benetton"),
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": {"pink", "green"}},
}

# changing the number of stores from 7000 to 2
brand["number_stores"] = 2

# printing the name of Zara's cleints
print(f"Zara's clients are: {', '.join(brand['creator_name'])}")

# adding a new item to the dictionary
brand.update({"country_creation": "Spain"})

# Checking if international competitos is in the dictionary --> if it is then adding a new value to it
if "international_competitors" in brand:
    current_value = brand["international_competitors"]
    if isinstance(current_value, tuple):
        brand["international_competitors"] += ("Desigual",)
    else:
        brand["international_competitors"] = (current_value, "Desigual")
else:
    brand["international_competitors"] = ("Desigual",)

# Deleting the creation date from the dictionary
brand.pop("creation_date")

# Getting the last international competitor in the list
last_competitor = brand["international_competitors"][-1]
print(f"The last international competitor in the list is: {last_competitor}")

# Printing the major colours of the US
print("The major colours in the US are: ", brand["major_color"]["US"])

# print length of dictionary
x = brand.keys()
print(len(x))

# print keys of dictionary
print(x)

# new dictionary
more_on_zara = {"creation_date": 1975, "number_stores": 10000}

# merging original dictionary with new dictionary
brand.update(more_on_zara)
print(brand)

# printing number of stores - shows the value from the new dictionary not the original dictionary
print(brand["number_stores"])
