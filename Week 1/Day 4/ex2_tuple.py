# you cannot add values to a tuple unless it is converted to a list and then turned back into a tuple after

my_numbers = (2, 4, 5, 6, 8)
my_list = list(my_numbers)
my_list.append(9)
my_numbers = tuple(my_list)
print(my_numbers)
