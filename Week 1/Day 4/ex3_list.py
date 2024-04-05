basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")

basket_count = basket.count("Apples")

print(basket)
print("The number of Apples in my list are: ", basket_count)

basket.clear()
print(basket)
